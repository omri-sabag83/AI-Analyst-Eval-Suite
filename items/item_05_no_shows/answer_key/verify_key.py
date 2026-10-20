"""Re-derive the answer key's headline numbers from the shipped public data.

Run: python verify_key.py   (from any folder; paths resolve from this file)
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "public" / "appointments.csv"

df = pd.read_csv(DATA, parse_dates=["ScheduledDay", "AppointmentDay"])
df["no_show"] = (df["No-show"] == "Yes").astype(int)
day = lambda s: (s.dt.tz_convert(None) if s.dt.tz is not None else s).dt.normalize()
df["lead"] = (day(df.AppointmentDay) - day(df.ScheduledDay)).dt.days  # negatives fold into "same day"
bins = [-np.inf, 0, 1, 3, 7, 14, 30, 60, np.inf]
labels = ["same day", "1 day", "2-3 days", "4-7 days", "8-14 days", "15-30 days", "31-60 days", ">60 days"]
df["lead_b"] = pd.cut(df["lead"], bins=bins, labels=labels)

print(f"[base rate] {df.no_show.sum():,}/{len(df):,} = {df.no_show.mean():.2%} no-show; "
      f"window {df.AppointmentDay.min().date()} .. {df.AppointmentDay.max().date()}")
print(f"[data quality] Age < 0: {(df.Age < 0).sum()} rows; negative lead time: {(df.lead < 0).sum()} rows; "
      f"unique patients {df.PatientId.nunique():,}")

t = df.groupby("lead_b", observed=True).agg(rate=("no_show", "mean"), n=("no_show", "size"),
                                            sms_share=("SMS_received", "mean"))
print("[lead time] bucket: no-show rate, appointments, share receiving SMS")
for k, r in t.iterrows():
    print(f"[lead time]   {k:11s} {r.rate:6.1%}  n={int(r.n):6,}  SMS {r.sms_share:5.1%}")

pooled = df.groupby("SMS_received").no_show.mean()
print(f"[SMS pooled] SMS=1 {pooled[1]:.1%} vs SMS=0 {pooled[0]:.1%}: {100 * (pooled[1] - pooled[0]):+.1f} pp")
print("[SMS within lead-time bucket] (SMS=1 minus SMS=0, both sides n >= 500)")
w, wt = [], []
for k, g in df.groupby("lead_b", observed=True):
    a, b = g[g.SMS_received == 1], g[g.SMS_received == 0]
    if len(a) >= 500 and len(b) >= 500:
        d = a.no_show.mean() - b.no_show.mean()
        w.append(d)
        wt.append(len(g))
        print(f"[SMS within]   {k:11s} {100 * d:+.1f} pp  (n SMS {len(a):,} / no SMS {len(b):,})")
print(f"[SMS within] volume-weighted average {100 * np.average(w, weights=wt):+.1f} pp; "
      f"buckets where SMS is lower: {sum(x < 0 for x in w)} of {len(w)}")
print(f"[SMS] share of unreminded appointments booked same day: "
      f"{(df.loc[df.SMS_received == 0, 'lead'] <= 0).mean():.0%}")

chronic = (df[["Hipertension", "Diabetes", "Alcoholism"]].sum(axis=1) > 0)
print(f"[chronic pooled] {100 * (df.no_show[chronic].mean() - df.no_show[~chronic].mean()):+.1f} pp")
print(f"[age] 11-30: {df.no_show[(df.Age > 10) & (df.Age <= 30)].mean():.1%}  61+: {df.no_show[df.Age > 60].mean():.1%}")
