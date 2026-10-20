## The 14 gates (the standards)

1. **Claims tagged OBS / HYP / CON.** Every claim is marked observation
   (computed from the data), hypothesis (consistent but not shown), or
   conclusion (the reading the evidence best supports, residual uncertainty
   stated). A *mechanism supported by the data* is kept separate from a
   *real-world cause* (a hypothesis), and the extra data that would confirm the
   hypothesis is named.
   *Fix:* tag each untagged claim; demote any "cause" the data only makes
   plausible to `[HYP]` and state what would confirm it.

2. **Grain, coverage, time window stated.** One row per what; how many
   days / records; any partial or cut-off periods called out.
   *Fix:* add the one-line statement near the top of the write-up.

3. **Reconciled to the brief.** Any reference total, sample output or pivot the
   brief provides has been reproduced before the pipeline is trusted.
   *Fix:* run the reconciliation; if it does not tie, stop and explain the gap
   before any finding stands.

4. **Data-quality issues surfaced up front.** Nulls, duplicates, junk
   categories, censoring, definitional ambiguities are stated *before* the
   analysis, not buried in the caveats.
   *Fix:* move them into a "data & method" note ahead of the findings.

5. **Rate vs mix separated.** When a blended metric moves, the change is
   decomposed into a rate effect (per-group value moved) and a mix effect
   (weights moved); standardise before concluding behaviour changed. A blended
   metric can fall while every subgroup rate is unchanged.
   *Fix:* run the `mix_vs_rate` decomposition; restate the finding as whichever
   effect actually carries it.

6. **Correlated dimensions disentangled.** If two cuts both move, they are
   cross-tabbed to one mechanism, not reported as two separate causes.
   *Fix:* cross-tab the two dimensions; report the single cell / mechanism that
   drives it.

7. **Volume beside rate.** Every daily / segment view shows the count next to
   the rate, so a mix shift is not misread as a behaviour change.
   *Fix:* add the volume column / series to each rate view.

8. **Impact is a labelled counterfactual.** Any cost / impact figure is an
   explicit counterfactual (e.g. baseline rate x actual volume) and is called an
   estimate, not a measured loss.
   *Fix:* show the counterfactual construction; label it an estimate; state the
   assumption it rests on.

9. **Standing vs incident findings separated.** Chronic / structural issues are
   kept apart from the specific incident under investigation - the brief usually
   wants both.
   *Fix:* split the findings into "the incident" and "standing" sections.

10. **A single snapshot is not a trend.** If asked "is X getting worse" from one
    as-of extract: the only directly observed quantity is the raw event *count*
    over time; any reconstructed *rate* needs a denominator the snapshot lacks,
    and a fixed sample shrinks that denominator on its own, so a rising
    reconstructed rate is an artefact.
    *Fix:* report the raw count and its direction; name the real data
    (population / enrolment over time) a rate would need; still give the answer
    the count supports.

11. **Implausible base rate / undefined label challenged.** A headline like 68 %
    churn, or any label with no written definition, is itself a finding: the
    sample is likely not the population, every number is kept "within-sample",
    and the definition + sampling method are requested.
    *Fix:* add the within-sample framing and the ask; quote no figure as a
    population rate.

12. **Censored / weak-signal result not oversold.** When the strongest
    association is a few points on a high base and the recent window is
    right-censored, the deliverable is a diagnosis + a short list of data to
    pull next - not a multi-recommendation programme.
    *Fix:* downgrade the action plan to a diagnosis + next-data list; mark the
    censored window.

13. **Leakage guard.** Columns mechanically tied to the outcome or the as-of
    snapshot (recency proxies) are reported in their own section and kept out of
    any driver / factor ranking.
    *Fix:* pull those columns out of the ranking; report them separately as
    "sits on top of the outcome".

14. **Arithmetic hygiene & internal consistency.** The first 13 gates test how
    the analysis *reasons*; this one tests whether the *numbers themselves* hold
    up. A finding is not sound just because the reasoning around it is. Check
    each of:
    - **Denominator match.** Every "X% of", "share of", "over- / under-
      represented", "N times more likely" draws its numerator and its comparison
      base from the *same population at the same grain* - senders compared to
      senders, not senders to transactions; this month's payers to this month's
      actives, not to all-time actives. A ratio whose top and bottom count
      different things is meaningless.
    - **Equal exposure when pooling or normalising.** Any per-day, per-capita,
      per-user, indexed or multi-period figure assumes every unit in the base
      had comparable exposure. Partial periods, truncated windows, short months,
      right-censored recent buckets and unequal follow-up must be dropped or
      weighted - never averaged in raw. (A day-of-month index built from a
      31-day and a 28-day month mechanically halves days 29-31.)
    - **Findings don't contradict each other.** No headline claim conflicts with
      another headline claim or with a stated framing fact. Where two sections
      describe the same quantity, the numbers tie. ("A quarter of 'free'
      transfers are billed" and "the feature is free for most users" cannot both
      stand.)
    - **Round-trip the load-bearing numbers.** Re-derive the two or three
      figures the conclusions rest on by a second method or from a different
      table, and confirm they match.
    *Fix:* recompute the figure with the base corrected, the exposure equalised,
    or by an independent route; reconcile any two findings that disagree before
    either is quoted. Run this gate as the holistic read described in *How to run
    it*, not purely line by line.


<!-- Extracted verbatim from ~/.claude/skills/analysis-rigor-pass/SKILL.md (Claude-Skills repo commit 30c7076) by runner/common.py extract_gates() -->
