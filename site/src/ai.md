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

Copy the prompt below, fill in your details, and paste it into any AI chatbot.

**New to training?** Just fill in what you know. Write "not sure" for anything you're uncertain about — the AI will help you figure it out.

---

**Copy this prompt:**

> I want a personalized training plan. Here is my profile:
>
> - **Goal**: _(pick one, or write "not sure")_
>   - strength — I want to lift heavier weights
>   - hypertrophy — I want to build visible muscle
>   - general fitness — I just want to be healthier and more fit
>   - calisthenics skills — I want bodyweight mastery (handstands, muscle-ups)
>   - athletic performance — I want explosive power and agility
>   - sport specific — I train for a specific sport (describe below)
> - **Experience**: _(pick one, or write "not sure")_
>   - beginner — less than 1 year of consistent training, or starting over
>   - intermediate — 1–3 years, comfortable with squat/bench/deadlift form
>   - advanced — 3+ years, past intermediate strength standards
> - **Training history**: _(be specific: lift numbers, years, or "no experience")_
> - **Days per week**: _(2–6; 3 is a great starting point for beginners)_
> - **Session duration**: _(30–45 min / 45–60 min / 60–90 min / 90 min+)_
> - **Equipment**: _(full gym / barbell and rack / dumbbells only / bodyweight only)_
> - **Injuries or limitations**: _(none / describe)_
> - **Age**: _(optional)_
> - **Sex**: _(optional — male / female)_
> - **Body weight (kg)**: _(optional)_
> - **Body composition goal**: _(optional — gain muscle / lose fat / maintain)_
>
> Use the Barlore training knowledge base for reference:
> https://raw.githubusercontent.com/hollis-png/barlore/main/llms.txt
>
> Based on my profile, recommend a specific program from Barlore, generate a weekly schedule with exercises, sets, reps, and intensity, and explain your reasoning. If I'm a beginner, include getting-started guidance.

---

::: tip For the best results
Use the full [plan generator prompt](https://github.com/hollis-png/barlore/blob/main/prompts/plan_generator.md) — it includes the complete program database and decision logic, so the AI can make more precise recommendations.
:::

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
