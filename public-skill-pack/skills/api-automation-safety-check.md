---
name: api-automation-safety-check
description: Safety checklist for browser automation, scraping, undocumented API reconstruction, OpenAPI generation from browser traces, and third-party service integrations.
---

# API Automation Safety Check

Use this before building automation against websites or services.

## Core Rule

`Technically possible` does not mean `allowed`.

## Inputs

- Target site or service.
- Who owns the site/data.
- Intended action.
- Whether official API/export exists.
- Whether login, cookies, API keys, payment, or personal data are involved.
- Whether the result is private, internal, public, or commercial.

Never paste passwords, API keys, cookies, or private user data into prompts.

## Checklist

1. Ownership: Is this your service, client-approved, public open data, or a third-party platform?
2. Permission: Do terms allow bots, scraping, API use, or data reuse?
3. Authentication: Does it touch login, paid content, private endpoints, CSRF tokens, or cookies?
4. Data rights: Will you collect or republish personal data, reviews, images, prices, or copyrighted content?
5. Rate limits: How often will it run? Could it burden or trigger the site?
6. Secrets: Do traces/logs contain cookies, tokens, IDs, emails, or hidden endpoints?
7. Stability: What happens when the site changes?
8. Human approval: Does it post, buy, reserve, delete, message, or publish anything?

## Decision

```
【Decision】
OK / OK with limits / Needs permission / Do not build

【Why】
- xxx

【Safer Alternative】
- Official API:
- CSV/export:
- Manual upload:
- Internal-only workflow:

【Conditions if built】
- Rate limit:
- Secret redaction:
- Human approval:
- Monitoring:
```

## Hard No

- Bypassing login, paywalls, CAPTCHA, or access controls.
- Ticket/stock/reservation monitoring for resale or unfair advantage.
- Automated scraping or posting where platform rules prohibit it.
- Collecting or reselling personal data without permission.
- Sharing captured cookies, tokens, or private endpoints.
