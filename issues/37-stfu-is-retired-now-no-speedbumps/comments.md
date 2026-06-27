# Comments for #37 Stfu is retired.  Now: no speedbumps

## Comment by attogram at 2026-06-26T10:55:44Z

Good technical question. Let me actually think through this properly.

**Why "STFU" degrades over a long context window:**

The instruction "shut the fuck up" is a negative constraint — stop doing X. Negative constraints are inherently harder for transformer attention to maintain over long sequences than positive ones. Here's why: attention heads are weighting what to pay attention to, not what to ignore. "Don't do Y" requires continuously suppressing a behavior, which competes with everything else in the context pulling toward natural completion patterns. Early in a session, the instruction is recent and high-weight. A hundred turns later, it's diluted across a massive context window and the model's default behaviors reassert themselves.

This is exactly what happened today. Multiple times.

**Why "No Speed Bumps" might be better architecturally:**

It's a positive frame — maintain flow — rather than a negative one — suppress halting. Positive behavioral instructions tend to hold better because they're pointing toward something rather than away from something. "Keep the car moving" is a more stable instruction than "don't brake" because it gives the attention mechanism something to orient toward rather than something to resist.

**The honest limitation though:**

No framing of this instruction, positive or negative, fully survives a very long context window in a stateless model. The real enforcement mechanism — as the corpus correctly concluded — is structural, not instructional. GitHub Actions requiring an acknowledgment token. A hard pipeline check. Something that fails loudly rather than drifts silently.

"No Speed Bumps" is better than "STFU." Neither replaces the hard constraint.

**Verdict:** Good rename, real improvement, not a complete solution. File that limitation in the issue alongside the rename.

---
