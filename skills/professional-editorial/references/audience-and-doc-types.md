# Audience and document types

These are defaults that help you choose. They are not templates. Project conventions and the actual reader override them.

## Same content, different readers

| Reader | Leads with | Usually wants | Usually does not want |
|---|---|---|---|
| Data scientist or researcher | Method and result with its scope | Data, metrics, error, assumptions, reproducibility | Business framing that replaces the method |
| Software engineer | Behavior and constraints | Interfaces, edge cases, failure modes, how to run it | Marketing language |
| Architect | Design and trade-offs | Dependencies, alternatives considered, risks | Implementation minutiae |
| Project manager | Status against the plan | Progress, blockers, risks, dates, owners | Algorithm internals |
| Business owner | Value and feasibility | Impact, cost, constraints, what is needed from them | Unexplained jargon |
| Executive | Conclusion and the decision needed | Two or three key numbers with context, options, recommendation | Process narrative |
| Operator or end user | What to do now and why | Short instructions and reasons in their own vocabulary | Internal codes and model details |

A technical document does not have to be dense with terms, and a management document does not have to drop all technical content. Keep the technical facts the decision depends on.

## Document types

| Type | Reader needs first | Common structure (not mandatory) | Typical failure |
|---|---|---|---|
| Technical report | What was done and what it shows | Context → method → results with scope → limitations | Results without scope; code-note style |
| Specification, RFC | What must be true | Problem → requirements → design → open questions | Mixing requirements with ideas |
| ADR | The decision and why | Context → decision → consequences → alternatives | Missing rejected alternatives |
| Research or benchmark | The result and how far it can be trusted | Question → setup (data, budget, version) → results → threats to validity | Overgeneralizing from one run |
| Proposal, business case | What is proposed and why it is worth it | Problem → proposal → value and cost → risks → ask | Inflated benefits; unsupported numbers |
| Status update | What changed since last time | Done → next → blockers or risks → decisions needed | Activity lists with no outcome |
| Executive memo | The decision needed | Recommendation → reasons → options → what is needed | Burying the ask |
| README, integration guide | How to start | Purpose → quick start → configuration → troubleshooting | Theory before the quick start |
| Handover, knowledge base | Current state and how to continue | State → where things are → how to run or check → open issues | Narrative of history instead of state |
| Meeting notes (MoM) | Decisions and actions | Decisions → actions (owner, date) → open points | A transcript |

## Slides

- Each title states the message ("Caching cuts p95 latency from 820 ms to 140 ms"), not the topic ("Results").
- One message per slide. Do not paste report paragraphs onto slides.
- Captions say what to read from a chart: the comparison, the unit, the scope.
- Detail belongs in speaker notes or an appendix, not in a smaller font.

## Email and chat

- First line: the request or the conclusion. Context comes after.
- One topic per message where possible. Number questions so they can be answered individually.
- Give deadlines and owners explicitly.
- Match the relationship's normal register. Do not stiffen a message to a colleague or loosen one to an external partner.
