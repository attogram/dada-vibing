Skill: Issues Sync (v0.1)

ROCK

   Context: Janitorial agent task. Run periodically or on demand. Goal:
   Local issues/ = exact replica of GitHub source of truth. Method: gh CLI
   → JSON → write raw body per issue. No reformatting. No headers. No
   metadata. Output: issues/[NNN]-[Code]-[Summary]/[code-summary].md +
   ISSUES.md TOC.

PROSE

1. Purpose

   This skill synchronizes the local issues/ directory with the GitHub
   Issues source of truth. Every [code-summary].md file must be a
   byte-for-byte exact replica of the GitHub issue body and all comments —
   no headers, no metadata, no reformatting, no summarization. Lossless.

2. Prerequisites

     * gh CLI or curl for API access
     * Repository: attogram/dada-vibing
     * Python 3 (for JSON processing)

3. Ingestion Protocol (Lossless)

   - Fetch all issues (including closed) and all comments.
   - For each issue:
     - Directory: `issues/[NNN]-[Code]-[Summary]/`
     - File: `[code-summary].md`
     - Content: Full issue body + \"---\" separator + All comments (chronological).

4. Source of Truth

   The GitHub Issues are the absolute source of truth. The repo is a local
   mirror for research and triage.

5. Implementation (curl/API)

   ```bash
   curl -s -H \"Accept: application/vnd.github.v3+json\" \
     \"https://api.github.com/repos/attogram/dada-vibing/issues?state=all&per_page=100\"
   ```
   Comments per issue:
   ```bash
   curl -s -H \"Accept: application/vnd.github.v3+json\" \
     \"https://api.github.com/repos/attogram/dada-vibing/issues/{number}/comments\"
   ```
