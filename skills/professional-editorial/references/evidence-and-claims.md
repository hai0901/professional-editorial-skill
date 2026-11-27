# Evidence and claims

The goal is that the strength of each statement matches what is known. This is not about adding hedges everywhere. Unnecessary qualification is a defect too.

## Status of information

| Status | How to write it | English cue | Vietnamese cue |
|---|---|---|---|
| Fact | State it directly | "The service runs on…" | "Service chạy trên…" |
| Verified result | Result plus the scope of verification (data, run, date, budget) | "On dataset X, run Y, …" | "Trên bộ dữ liệu X, lần chạy Y, …" |
| Observation | Describe what was seen, without generalizing | "In this run, …" | "Trong lần chạy này, …" |
| Inference | Conclusion plus the basis for it | "Because…, this suggests…" | "Vì…, điều này cho thấy…" |
| Hypothesis | Mark it as untested | "A possible explanation is…" | "Một giả thuyết là…" |
| Proposal | Mark it as a recommendation | "We propose…" | "Đề xuất…" |
| Assumption | Name it where it affects the result | "Assuming…" | "Giả định…" |
| Unknown | Say it is unknown; do not fill the gap | "Not yet measured." | "Chưa đo." |
| Conflicting evidence | Present both sources and the impact; do not pick a side without grounds | "Source A says…, source B says…; this affects…" | "Nguồn A ghi…, nguồn B ghi…; ảnh hưởng…" |

## Concepts that must not be conflated

| A | B | Difference |
|---|---|---|
| Feasible | Optimal | Satisfying constraints is not the same as being the best |
| Optimal in a model | Optimal in reality | A solver's `OPTIMAL` holds only for the model it solved, which may be relaxed or simplified |
| Simulated | Measured | Simulation output is not operational data |
| Synthetic or research data | Operational data | Results do not transfer without validation |
| Tested | Validated | Passing tests does not show that requirements are met |
| Proposed or designed | Implemented | A design is not code; code is not deployment |
| Prototype | Production system | Different guarantees |
| Forecast | Actual | Predicted is not observed |
| Correlation | Causation | Co-movement does not establish a cause |
| Accuracy | Precision (classification) | Different metrics |
| Precision | Recall | False alarms versus misses |
| Median (P50) | Mean | Not interchangeable, especially for skewed data |
| Authentication | Authorization | Identity versus permission |
| Improvement in one scenario | General improvement | Report the scope |

## Reporting results

- Give the scope with every result: dataset or fixture, scenario, run, time budget, date, version. The reader should be able to tell what the number covers.
- Keep caveats next to the numbers they qualify. A caveat moved to an appendix no longer protects the reader.
- "Best" or "better" only relative to what was actually compared, on the metric that was compared.
- No "significantly" or "clearly" without a test or an effect size that justifies it.
- Do not round numbers in a way that changes the conclusion, and do not add precision the measurement does not have (false precision).
- If one scenario shows a regression, report it. Do not average it away.
- Separate "what happened" from "why we think it happened".

## Flagging issues during editing

In proofreading, rewriting, summarizing and translating, you may notice a statement that looks technically wrong: two numbers that disagree, a claim the code does not support, a scope statement contradicted elsewhere in the document. Do not fix it silently. List it separately:

- the location and the exact text,
- why it looks wrong, with evidence (another section, a source file and line, a log),
- what would resolve it.

Check the evidence yourself when that is cheap, for example by opening the referenced code or log. Say whether you checked or are only reporting a suspicion.
