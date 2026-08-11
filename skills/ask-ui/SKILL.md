---
name: ask-ui
description: Render two or more independent questions from an Agent workflow as a local interactive form, preselect recommended answers, save responses as portable JSON, and return submitted answers directly to the waiting Agent command. Use for grilling, brainstorming, requirement clarification, configuration, planning, or any workflow that needs to ask multiple questions at once. Also use the manual recovery path when the user says “已提交”, “提交好了”, or “答完了” after an active Ask UI round.
---

# Ask UI

Use Ask UI as a presentation and persistence adapter. Keep question generation and reasoning in the calling workflow.

## Decide whether to use the UI

Use the UI when the current round contains at least two independent questions that the user can answer now. Keep dependent questions for a later round. Ask a single question directly in the conversation.

If the local server or browser cannot start, fall back to the calling workflow's normal text format.

## Ask and wait for the answer

1. Resolve the directory containing this `SKILL.md` as `ASK_UI_SKILL_DIR`.
2. Read [references/schema.md](references/schema.md) before creating JSON.
3. Create a QuestionSet JSON file. For a new task, omit `sessionId`; for follow-up rounds, reuse the active `sessionId` and set `basedOnRound`.
4. Run the foreground command and keep the tool call active until it exits:

   ```text
   node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs ask --input <questions.json>
   ```

5. The command writes readiness details and the local URL to stderr, opens the form, and waits. Do not end the Agent turn or ask the user to reply “已提交”.
6. After the user submits, parse the single JSON result written to stdout and continue the originating workflow immediately.
7. If more independent questions are needed, call `ask` again with the same `sessionId` and `basedOnRound` set to the returned round. When no further questions remain, complete the session.

Use `--no-open` only when browser opening is managed separately. Use `--port <number>` only when a fixed localhost port is required.

## Manual fallback and recovery

Use the detached workflow when the foreground tool call cannot remain active, the local browser cannot reach the temporary server, or an interrupted direct round must be recovered:

```text
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs create --input <questions.json>
```

Parse the returned JSON. Include its URL and a visible marker in the conversation:

   ```text
   ask-ui-session: <sessionId>
   ```

Tell the user to submit the form and reply only with “已提交”. The `create` command starts or reuses a detached localhost server and returns immediately.

When the user says “已提交”, “提交好了”, or “答完了”:

1. Recover `sessionId` from the latest `ask-ui-session` marker in this conversation.
2. Run:

   ```text
   node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs resume --session <sessionId>
   ```

3. If the result is `submitted`, use its questions and answers to continue the original workflow.
4. If more independent questions are needed, prefer returning to the foreground `ask` command with the same `sessionId` and `basedOnRound` set to the processed round. Use `create` again only when direct waiting remains unavailable.
5. If no further questions remain, run:

   ```text
   node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs complete --session <sessionId>
   ```

If the conversation marker is unavailable, run `resume` without `--session`. When multiple candidates are returned, infer the best match from the current topic, workspace, title, and submission time. Ask the user only when the match is genuinely ambiguous.

Repeated “已提交” messages must not create duplicate rounds. A new round should only be created after successfully reading a `submitted` round.

## Preserve session continuity

- One task is one Session.
- Each batch of questions is one Round.
- Reuse `sessionId` across all rounds of the same task.
- Never overwrite submitted questions or answers.
- Put corrections and additional confirmation in a new Round.
- Start a new Session only for a new task, a completed task, or an explicit restart.

## Optional active wake-up

Ask UI supports optional wake metadata for Claude Code and Codex App Server. Treat it as an enhancement, not a requirement.

- Enable automatic wake only with the user's consent.
- Claude Code requires a recorded session id.
- Codex requires a host-provided thread id. Never guess a Codex thread id.
- On adapter failure, preserve the answer and return to the manual “已提交” workflow.
- Direct `ask` mode never triggers wake adapters because the waiting process is already the return channel.

## Useful commands

```text
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs ask --input <questions.json>
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs create --input <questions.json>
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs status --session <sessionId>
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs serve
node <ASK_UI_SKILL_DIR>/scripts/ask-ui.mjs complete --session <sessionId>
node <ASK_UI_SKILL_DIR>/scripts/self-test.mjs
```
