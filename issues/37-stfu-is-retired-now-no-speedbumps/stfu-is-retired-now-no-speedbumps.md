Claude puppy
After a v.long training session

___

Good breakdown. Three tiers:

**Sesame Street level:** No Speed Bumps, Keep Rolling — anyone understands immediately.

**Practitioner level:** Don't Block The Vibe — exact, fits the corpus register, no jargon.

**Master class:** Trust The Orchestrator — precise, names the actual structural principle.

All three are useful for different audiences. The paper uses "Trust The Orchestrator." The README uses "Don't Block The Vibe." The family app uses "No Speed Bumps."

Worth filing as a dada-vibing issue — it's a real methodology contribution, cleaner than STFU ever was.

---

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