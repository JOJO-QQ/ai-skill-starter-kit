---
name: ai-workspace-design-check
description: Decide whether an AI task should be handled by chat, project memory, a reusable skill, a small tool, a connector, a plugin, or automation.
---

# AI Workspace Design Check

Use this before turning AI work into prompts, tools, or automations.

## Core Idea

Strong AI use is not only asking better questions.

Strong AI use means setting up the right workspace:

- `Chat`: one-off thinking.
- `Project/Memory`: stable background context.
- `Skill`: repeated procedure.
- `Small Tool/Artifact`: reusable form, checklist, calculator, page, or prototype.
- `Connector`: permitted external data.
- `Plugin/Extension`: one concrete repeated need.
- `Automation`: only after the manual workflow is clear and safe.

Use the smallest setup that works.

## Inputs

- What do you want AI to do?
- How often will you repeat it?
- What inputs are needed?
- What output do you want?
- Does it involve accounts, APIs, payments, personal data, posting, or public distribution?
- What part feels repetitive or risky?

Never paste passwords, API keys, cookies, billing details, or private customer data.

## Decision Guide

Use `Chat` if:
- It is one-off.
- The context is small.
- The output is disposable.

Use `Project/Memory` if:
- You repeat the same background explanation.
- Tone, audience, rules, or project context should persist.

Use `Skill` if:
- You repeat the same task.
- The steps and output format matter.
- There are recurring checks or warnings.

Use `Small Tool/Artifact` if:
- A form, checklist, calculator, table, or preview would make the task easier.
- You want to test demand before building a full app.

Use `Connector` if:
- AI needs external data.
- You have permission.
- Manual export is not enough.

Use `Plugin/Extension` if:
- It solves one repeated concrete problem.
- It does not duplicate existing tools.

Use `Automation` if:
- The manual workflow is already clear.
- Failure modes are understood.
- Human approval is required for posting, payment, deletion, sending, or publishing.

Use `Custom Slash Command` if:
- You repeat the same narrow prompt often.
- You want to call it manually with `/command`.
- The workflow is simple enough to fit in one Markdown prompt file.

Use `Skill` instead if:
- The workflow has multiple steps.
- It needs validation rules.
- It has safety warnings.
- It should be reused across related tasks.

Use `Separate Planning Session` if:
- The task is large or risky.
- Many ideas were discussed.
- Some approaches were rejected.
- The implementation should follow one approved plan.

Give the implementation session a short handoff: goal, approved plan, target files, risks, tests, and stop conditions.

## Output

```
【Recommended Setup】
Chat / Project / Memory / Skill / Small Tool / Connector / Plugin / Automation

【Why】
- xxx

【Start Small】
- First:
- Not yet:

【Safety Check】
- Secrets:
- Cost:
- Personal data:
- Posting/publishing:
- Terms of service:

【Next Steps】
1. xxx
2. xxx
3. xxx
```

## Rules

- Do not build a complex system before a simple workflow works.
- Do not install tools just because they sound powerful.
- Verify third-party skill/plugin install commands from official sources before running them.
- Do not treat viral "command lists" as official built-in commands. Use them as naming inspiration only.
- Do not store unstable facts as permanent memory.
- Public versions must remove secrets, local paths, private account details, and risky automation instructions.
