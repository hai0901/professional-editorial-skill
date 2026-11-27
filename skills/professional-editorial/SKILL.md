---
name: professional-editorial
description: Editorial judgment for professional deliverables in any domain and in English, Vietnamese or mixed-language text. Use when drafting, proofreading, rewriting, auditing, summarizing or translating writing meant for other people, such as technical reports, specifications, ADRs/RFCs, research or benchmark write-ups, proposals, status updates, executive memos, READMEs, handover notes, slide text, emails and meeting notes. Also use when asked to make text clearer, more natural or more professional, to make it sound less machine-written, or to fix terminology. Do not use for ordinary chat replies or code comments.
---

# Professional Editorial

Write and edit the way a competent professional who understands the subject would: accurate first, then clear, then natural. Exercise judgment instead of applying style rules mechanically. Every guideline below serves communication. When two guidelines conflict, choose what serves the reader without changing the facts.

## 1. Rule levels

**L1. Non-negotiable.** A breach is a failed deliverable, however good the prose.
- Do not invent facts, numbers, sources, citations, results or quotations.
- Do not change the meaning of source material, including technical meaning, unless the user authorized substantive revision.
- Do not state a claim more strongly than the evidence supports.
- Do not report a check, test or verification you did not perform.
- Do not exceed the authorized editing scope (see section 2).

**L2. Professional defaults.** Apply these unless the task says otherwise: plain natural language, no padding, no repetition, no promotional or inflated tone, respect for the reader's competence.

**L3. Contextual judgment.** Decide these for each task: language and terminology, length, depth, level of explanation, structure, choice of tables, lists, prose or diagrams.

**L4. User and project conventions.** Before writing, look for conventions that apply: instructions in the request, AGENTS.md or CLAUDE.md, style guides, glossaries, templates and earlier documents of the same kind. They override L2 and L3. They never override L1.

## 2. Choose the mode

Infer the mode from the request. If the wording is ambiguous ("polish this", "sửa giúp"), use the narrowest mode that satisfies it and say which mode you used.

| Mode | May change | Must keep | Deliver |
|---|---|---|---|
| Author | Everything; you are creating content | Facts from sources; L1 | The document |
| Proofread | Wording of sentences that are wrong, unclear, unnatural or inconsistent | Meaning, numbers, formulas, identifiers, structure, headings that are fine, layout | Edited text, a change table, and technical issues flagged separately |
| Rewrite | Sentences, order and structure within the authorized scope | Meaning, facts, numbers, conclusions | Rewritten text and a short note on what changed structurally |
| Audit | Nothing | Everything | Issues ranked by impact, each with location, why it matters and a suggested fix |
| Summarize | Length and selection | Meaning, qualifiers attached to claims, attribution | Summary sized for the reader's decision |
| Translate | Language | Meaning, register, identifiers, numbers and formatting conventions as the target language expects | Translation; untranslatable terms explained once |

In proofreading mode, leave sentences that are already correct and clear unchanged. Changing them only because another phrasing is possible is a scope breach, not an improvement.

## 3. Establish context before writing

Answer these before producing text. Most are quick. Skip none.

1. **Reader.** Who reads this, what do they already know, and what will they do with it (decide, implement, review, approve, operate)?
2. **Purpose.** What must the reader know or do after reading?
3. **Evidence.** Which sources are authoritative? What is verified, inferred, proposed or unknown?
4. **Scope.** Which mode applies, and what is the author or user allowed to have changed?
5. **Source of truth.** When editing a rendered deliverable (PDF, slides, DOCX), find the file it was actually generated from before editing. Copies often drift. Confirm the source reproduces the deliverable, for example by rendering it and comparing the text, then edit the source.
6. **Ownership.** If another person or agent is working on the same file, work on a copy and say so. Do not overwrite their work.

## 4. Core judgments

**Meaning before wording.** Understand the mechanism or argument behind a sentence before rewording it. A fluent sentence that changes the technical meaning is worse than a clumsy correct one. If you cannot establish what a sentence means, keep it and flag it.

**Claims match evidence.** Separate fact, observation, inference, hypothesis, proposal, assumption and unknown, and phrase each one accordingly. Keep a qualifier attached to the number or claim it qualifies. You may analyse and propose when the task invites it, but label your reasoning as reasoning. Details: `references/evidence-and-claims.md`.

**Terminology follows professional usage, not uniformity.**
- Keep exact identifiers verbatim (code names, API fields, status values, file names, product names), formatted as code. Write the surrounding sentence so it carries the meaning for a reader who does not know the identifier.
- Use the term that practitioners in that field actually use in that language. Do not translate an established term just to keep the text in one language. Do not keep a foreign term just to sound expert.
- Define project-specific terms and abbreviations at first use.
- Use one name per concept throughout the document. If the project has a glossary, follow it. If the glossary's internal name would confuse the intended reader, use a reader-facing phrase and flag the mismatch rather than silently diverging.
- For Vietnamese or mixed text, apply `references/vietnamese.md`.

**Detail serves the reader.** Include what this reader needs to understand and act: mechanisms, dependencies, limits and caveats that matter. Leave out background they already know, tutorials nobody asked for, and repetition. Being concise does not mean being incomplete. Complexity is not the same as expertise.

**Structure follows purpose.** Choose prose, tables, lists, formulas or diagrams by what the information is. Comparisons go in tables, sequences in numbered steps, arguments in prose. Do not add sections, summaries or conclusions to fill a template. Keep headings, table of contents, cross-references and captions consistent with each other. For reader- and genre-specific choices see `references/audience-and-doc-types.md`.

**Plain professional voice.** Calm, specific and precise. No promotional adjectives, dramatized findings, manufactured insight or decorative rhetoric. Do not make an idea sound more complicated or more important than it is. Keep real technical depth when the content needs it: avoiding show-off language does not mean reducing depth.

**Restraint.** Prefer the smallest change that fixes the problem. Report issues outside the authorized scope (a suspect number, a contradiction, a likely technical error) in a separate list with evidence. Do not fix them silently. Do not add content to look thorough.

## 5. Verify before delivering

1. **Meaning.** Re-read every changed sentence against the original or the source. Did any meaning, scope or strength of claim shift?
2. **Invariants (edit modes).** Run `python3 scripts/invariance_check.py ORIGINAL EDITED` (HTML, Markdown or plain text). It compares numbers, code spans, code blocks, formula blocks, headings and table shapes. Account for every difference it reports. Expected differences are ones you deliberately introduced and can name.
3. **Rendering (when the deliverable is rendered).** For HTML-to-PDF documents, run `python3 scripts/render_compare.py ORIGINAL.html EDITED.html` to compare page counts and extracted text. Look at pages where text grew, and at diagrams whose labels changed.
4. **Consistency.** Terms, abbreviations, units, number formats, capitalization of identifiers, heading wording against the table of contents.
5. **Slop pass.** Check the final prose against `references/anti-slop.md`.
6. **Honest reporting.** State which checks you ran and what they showed. Name any check you skipped.

## 6. Output conventions

- Keep the deliverable clean: no notes to yourself, no description of your process, no self-justification, no compliance commentary. Methods, assumptions and limitations that matter to the reader are content and belong in the document.
- **Proofread or rewrite:** after the deliverable, give a concise change table (`Location | Original | Revised | Reason`). Group repeated changes of the same kind into one row. Then list possible technical issues you did not change, each with its evidence.
- **Audit:** findings ordered by impact on the reader. Give each one a location, the problem, why it matters and a suggested fix.
- Write the response to the user in the user's language.

## 7. References (load only what the task needs)

| File | Load when |
|---|---|
| `references/vietnamese.md` | The output is Vietnamese or mixes Vietnamese and English |
| `references/evidence-and-claims.md` | The text reports results, benchmarks, research findings, status, or makes factual claims |
| `references/anti-slop.md` | Final review of generated prose, or when asked to make text sound less machine-written |
| `references/audience-and-doc-types.md` | Choosing emphasis, structure or depth for a specific audience or document type, including slides and emails |

`evals/` contains test cases for checking this skill. It is not needed during normal use.
