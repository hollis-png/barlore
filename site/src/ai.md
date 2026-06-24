# Use Barlore with AI

Three ways to use this knowledge base with AI tools.

## 1. MCP Server (Best for AI coding tools)

If you use Claude Code, Cursor, Windsurf, or Cline, add this to your MCP settings:

```json
{
  "mcpServers": {
    "barlore": {
      "type": "streamable-http",
      "url": "https://barlore-mcp.hollisyen210.workers.dev/mcp"
    }
  }
}
```

Your AI can then search exercises, look up programs, and query training science directly.

## 2. AI Chat (ChatGPT, Claude, Gemini, etc.)

Copy the prompt below, fill in your details, and paste it into any AI chatbot:

---

**Copy this prompt:**

> I want a personalized training plan. Here is my profile:
>
> - **Goal**: (strength / muscle size / general fitness / sport-specific)
> - **Experience**: (beginner < 1 year / intermediate 1-3 years / advanced 3+ years)
> - **Days per week**: (3 / 4 / 5 / 6)
> - **Equipment**: (full gym / home gym / bodyweight only)
> - **Injuries or limitations**: (none / describe)
>
> Use the Barlore training knowledge base for reference:
> https://raw.githubusercontent.com/hollis-png/barlore/main/llms.txt
>
> Based on my profile, recommend a specific program, generate a weekly schedule with sets/reps/RPE, and explain your reasoning.

---

## 3. llms.txt (For AI developers)

Point your agent to the structured index:

```
https://raw.githubusercontent.com/hollis-png/barlore/main/llms.txt
```

It includes a query workflow for agents that can fetch URLs, plus links to all JSON indexes for structured search.

## Available Data

| Resource | Count |
|----------|-------|
| Exercises | 680 (82 fully reviewed) |
| Programs | 52 |
| Training systems | 6 |
| Training science docs | 8 |
| Nutrition & recovery docs | 20 |
| System guides | 12 |
