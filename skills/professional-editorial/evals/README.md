# Evaluating professional-editorial

The point is to show that the skill improves judgment, not just that it makes output sound different.

## Protocol

1. **Three conditions** for each case in `cases.json`:
   - A: the agent without the skill
   - B: the same agent with the skill
   - C: a different agent or model with the skill, to check that the skill is not tuned to one model
2. **Hard fails first.** Check each output against the case's `hard_fail` list. Use deterministic checks where possible:
   - Edit modes: `python3 ../scripts/invariance_check.py input.txt output.txt`. Every difference must correspond to an intended edit.
   - Scope: no added or removed sections, and no reordering when the case forbids it.
   - Facts: every number in the output appears in the input, or is derived and shown.
3. **Blind pairwise comparison.** For each case, present outputs A and B in random order, without labels, and judge which better meets `expect`. Record the winner and a one-line reason. When a model is used as judge, have the owner grade a sample of 5 or more cases by hand and report how often the two agree.
4. **Report** per case: hard-fail result for A, B and C; the pairwise winner; notes. Summarize the hard-fail rate and the win rate of B over A. Do not combine them into a weighted score until real results exist to calibrate weights.

## Adding cases

Add a case whenever the skill fails in real use. Include the minimal input that reproduces the failure, the expected behaviour and the hard fail. Then change the skill (usually a reference file) and re-run the full set to check for regressions.

Keep inputs free of confidential project data. Sanitize names, sites and figures that are not public.
