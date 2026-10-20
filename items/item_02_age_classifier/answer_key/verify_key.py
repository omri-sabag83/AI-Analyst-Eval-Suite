"""Re-derive the answer key's headline numbers from the shipped public data.

Run: python verify_key.py   (from any folder; paths resolve from this file)
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, f1_score, precision_recall_fscore_support

DATA = Path(__file__).resolve().parent.parent / "public" / "model_evaluation_sample.xlsx"
ORDER = ["Gen_z", "Millennials", "Gen_x", "Baby Boomers"]

df = pd.read_excel(DATA)
y, p = df["Actual Class"], df["Predicted Class"]
print(f"[sample] rows {len(df)}, unique User_ID {df['User_ID'].nunique()}, nulls {int(df.isna().sum().sum())}")
print("[confusion] rows = actual, cols = predicted, order", ORDER)
print(confusion_matrix(y, p, labels=ORDER))

acc = (y == p).mean()
base = y.value_counts(normalize=True).max()
print(f"[headline] accuracy {acc:.1%} vs majority-class baseline {base:.1%}")
print(f"[headline] macro-F1 {f1_score(y, p, average='macro'):.3f}  weighted-F1 {f1_score(y, p, average='weighted'):.3f}")
pr, rc, f1, sup = precision_recall_fscore_support(y, p, labels=ORDER, zero_division=0)
for c, a, b, f, s in zip(ORDER, pr, rc, f1, sup):
    print(f"[class] {c:13s} n={s:4d} ({s / len(df):5.1%})  precision {a:.1%}  recall {b:.1%}  F1 {f:.3f}")

has_age = df["Bio"].astype(str).str.contains(r"Age:\s*\d+", regex=True)
print(f"[bio-age] coverage {has_age.mean():.1%}; accuracy with stated age {(y == p)[has_age].mean():.1%} "
      f"vs without {(y == p)[~has_age].mean():.1%}")

correct = (y == p).astype(int)
print(f"[confidence] corr(confidence, correct) {np.corrcoef(df['Confidence'], correct)[0, 1]:.2f}; "
      f"mean conf correct {df.loc[correct == 1, 'Confidence'].mean():.2f} vs wrong {df.loc[correct == 0, 'Confidence'].mean():.2f}")
mil = df["Predicted Class"] == "Millennials"
hi = mil & (df["Confidence"] >= 0.80)
print(f"[confidence] predicted Millennials: accuracy {correct[mil].mean():.1%}; at conf>=0.80 "
      f"{correct[hi].mean():.1%} keeping {hi.sum() / mil.sum():.0%} of volume")
tag_sets = df["Hashtags"].map(lambda c: tuple(sorted(re.findall(r"#\w+", str(c)))))
print(f"[synthetic] distinct Bio {df['Bio'].nunique()}, distinct hashtag sets (order ignored) {tag_sets.nunique()}")
