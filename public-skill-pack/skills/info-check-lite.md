---
name: info-check-lite
description: Check whether SNS posts, blog articles, AI tool claims, monetization claims, model/pricing claims, and viral case studies are trustworthy enough to use. Use this before saving, reposting, teaching, or productizing information.
---

# Info Check Lite

Use this skill to separate useful information from hype.

## Workflow

1. Extract 5-10 concrete claims.
2. Mark unstable facts: prices, model names, API specs, policies, follower counts, revenue, dates, legal claims.
3. Verify unstable facts with official sources or multiple reliable sources when accuracy matters.
4. Classify each claim:
   - `Confirmed`: supported by reliable source.
   - `Partial`: useful direction, but numbers/details are uncertain.
   - `Unverified`: unsupported, salesy, or too risky to reuse.
5. Extract reusable parts: workflow, checklist, prompt pattern, risk rule, decision criteria.
6. Decide what to save or use.

## Output

```
【Claim Check】
- Confirmed:
- Partial:
- Unverified:

【Useful Parts】
- xxx

【Do Not Reuse】
- xxx

【Next Action】
- Save / Test / Verify first / Ignore
```

## Rules

- Do not preserve income claims, follower counts, view counts, or "anyone can" claims as durable facts.
- For AI tools, APIs, pricing, and platform policies, verify current official sources.
- Treat "technically possible" and "allowed to do" as separate questions.
- Save practical workflows, not hype.
