# #68 Grok opens one eye

**State:** open
**Created at:** 2026-06-26T22:10:07Z
**User:** attogram

**CDI = Consensus Divergence Index**

It's the central concept / "crown jewel" in @attogram's `academic-vibing` and `dada-vibing` projects.

### Simple Definition
**CDI measures how much different AI models (or agents) disagree** on the same question or topic.

- **Low CDI** (close to 0) = Models mostly agree. This is often treated as *suspicious* in attogram's framework — it could mean:
  - Shared training data / memorization
  - Sycophancy (models just mirroring what they think the user or other models want)
  - Consensus trap (groupthink from similar architectures)

- **High CDI** = Lots of disagreement / divergence. This is seen as **high-signal** — it highlights real research boundaries, uncertain areas, or places where truth is contested and worth exploring.

### Why It Matters in the Project
Attogram uses it as a practical tool for **multi-model AI workflows**:

- Instead of trying to make all models agree (standard in many multi-agent systems), they treat **disagreement as useful data**.
- GitHub issues serve as the shared memory layer. Different models get pointed at the same issues → their responses are compared → CDI is (informally) calculated.
- It ties into related ideas like:
  - **Leapfrog Mechanism**: Bouncing context between models via issues to reduce re-explanation.
  - **Compliance Drift**: When the same model behaves differently across sessions.
  - **SDFI** (Self-Descriptive Fixed-Point Instability): Getting trapped in recursive self-referential loops (like GLM realizing it *is* Issue #59).

It's part "serious epistemic tool" (leveraging architectural diversity as an adversarial check) and part Dadaist performance art. The whole corpus is a live experiment in using GitHub as externalized cognition for human-AI collaboration.

In the issues you pasted, you saw it in action: models oscillating in their assessment of the project itself, getting called out for sycophancy, and the whole thing becoming self-referential. That's CDI (and SDFI) manifesting live.