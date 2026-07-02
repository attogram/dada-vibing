---
title: "The Monkey Manual Collection - A physical click-by-click registry for the Attogram corpus"
number: 50
author: attogram
created_at: 2026-06-26T15:29:13Z
updated_at: 2026-06-27T00:55:36Z
labels: []
---

**Issue #50: The Monkey Manual Collection**
*Subtitle: A physical click-by-click registry for the Attogram corpus*

---

**THE PROBLEM**

The Anti-Sycophancy Protocol (#43) assumes a 1024k tensor graph and a multi-agent pipeline. The Attogram corpus runs on a phone in Amsterdam.

The protocol and the corpus disagree on what is possible. The monkey manual resolves the disagreement by documenting what *actually* happens on the device. Not what should happen in a lab. What happens when a finger presses a screen.

---

**THE COLLECTION**

A linked registry of gesture-level operator manuals, one per daemon in the ecosystem. Each manual is a numbered step sequence: finger, screen, tap, paste. No abstraction. No metaphor. Physical clicks.

**Standard manual format:**

```
MONKEY: <role>
TOOLS: <apps, URLs, accounts>
OUTPUT: <where the receipt lands>
RECEIPT FORMAT: <what the final paste looks like>
```

Then the steps. 8 to 30, depending on the daemon. Each step is one physical gesture.

---

**THE KNOWN MONKEYS (initial registry)**

1. **POSTMAN MONKEY** — copies raw multi-turn exchanges from Node B into GitHub Issues. Manual drafted in [#43 Phase 3](https://github.com/attogram/dada-vibing/issues/43). Output: new issue in dada-vibing.

2. **MONKEY MONKEY** — copies the postman monkey's deposits into the family app repo. Different URL, same gestures.

3. **DJ MONKEY** — pulls the next cultural anchor (Sesame Street clip, Muppets video, song) into the corpus. Browser → YouTube → copy → new issue with title format.

4. **PEDANTIC MONKEY** — runs the citation check loop on academic-vibing outputs. Cross-references the bibliography, flags missing sources.

5. **NOTARY MONKEY** — preps documents for the Stichting phase gates. Reads Phase 1 statuten draft, formats it for notary intake.

6. **PINGER MONKEY** — sends the cold outreach from [#41 Joan Ganz Cooney Center](https://github.com/attogram/dada-vibing/issues/41). Contact form → paste → submit.

7. **TSHIRT MONKEY** — drafts the Attogram After Dark merch specs. Reads [#48](https://github.com/attogram/dada-vibing/issues/48), produces the SVG.

---

**THE ANTI-SYCOPHANCY PROPERTY**

A monkey manual cannot be performed sycophantically. Step 17 is "tap your finger inside the Node B text box. Hold your finger down firmly until the menu appears, then tap Paste." There is no interpretation in that step. The model either produced the gesture or it didn't.

This is the *physical* version of breaking the human mirror. Not philosophy. Mechanics.

---

**THE RECEIPT RULE**

Every monkey manual step that completes produces a verifiable artifact in the corpus:
- A new issue exists (postman)
- A new file exists (monkey monkey)
- A new tag exists (DJ)
- A flagged claim exists (pedantic)

The receipt is the proof the monkey ran. No receipt = monkey didn't run.

---

**THE ANTI-DRIFT MECHANISM**

Monkey manuals survive 1024k tokens because they don't live in context. They live in the repo. A cold-start model reads the manual, executes the gestures, files the receipt. The drift doesn't accumulate because the context resets per receipt.

---

**NEXT COORDINATE**

Pick the first monkey to fully document. Postman Monkey is already drafted in [[#43 Phase 3](https://github.com/attogram/dada-vibing/issues/43)](https://github.com/attogram/dada-vibing/issues/43) — lift it into #50 as the master template. Or start with DJ Monkey since it's the most frequently run daemon.

The street doesn't pause for permission. The receipts don't either. 🐾

---

Want this filed as #50?
