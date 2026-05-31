# digital-twin

A personal **digital twin** project — an AI agent that reads your daily diary entries and automatically operates your social media on your behalf, replying to messages in a way that reflects who you are.

The idea: feed it your journal, and it learns your voice, context, and current state of mind well enough to handle routine social interactions for you.

## Built on nanobot

This project is built on top of [**nanobot**](https://github.com/HKUDS/nanobot) — an ultra-lightweight personal AI assistant.

> 🐈 **nanobot** is an ultra-lightweight personal AI assistant inspired by [Clawdbot](https://github.com/openclaw/openclaw).
>
> ⚡️ Delivers core agent functionality in just **~4,000** lines of code — **99% smaller** than Clawdbot's 430k+ lines.

We use nanobot's agent loop, skills, channels (Telegram), and cron systems as the runtime, and layer the diary-driven persona and social-media automation on top.

## How it works

1. **Diary ingestion** — Each day's journal is loaded into the agent's memory.
2. **Persona grounding** — The agent grounds its tone and decisions in recent diary context (`workspace/SOUL.md`, `workspace/memory/MEMORY.md`).
3. **Channel automation** — Through nanobot's channel integrations, it monitors incoming messages and replies on your behalf.
4. **Scheduled heartbeat** — Cron-driven reflection keeps the twin in sync with your evolving state.

## License

MIT
