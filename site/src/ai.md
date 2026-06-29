# Use Barlore with AI

Four ways to use this knowledge base with AI tools.

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

### Available MCP Tools

| Tool | Description | Example |
|------|-------------|---------|
| `list_programs` | Browse programs by goal, system, or level | `list_programs(goal="hypertrophy", level="beginner")` |
| `search_exercises` | Search by name, pattern, equipment, or muscle | `search_exercises(pattern="hinge", equipment="barbell")` |
| `get_exercise` | Full exercise detail (EMG, cues, sources) | `get_exercise(id="back_squat")` |
| `search_by_muscle` | Find exercises targeting a specific muscle | `search_by_muscle(muscle_id="biceps_brachii")` |
| `get_program` | Full program with schedule and progression | `get_program(id="starting_strength")` |
| `get_training_concept` | Training science docs | `get_training_concept(concept="hypertrophy_mechanisms")` |
| `list_muscles` | All muscles with exercise counts | `list_muscles()` |

## 2. Get a Training Plan (AI Chat)

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
> Based on my profile, recommend a specific program from Barlore. Include:
> 1. A weekly schedule with exercises, sets, reps, and intensity
> 2. Progression rules — how to add weight, when to add it, how much, and what to do when I stall
> 3. Getting-started guidance if I'm a beginner

---

::: tip For the best results
Use the full [plan generator prompt](https://github.com/hollis-png/barlore/blob/main/prompts/plan_generator.md) — it includes the complete program database, decision logic, and progression rule templates so the AI gives you a plan with built-in weekly advancement, not just a static schedule.
:::

## 3. Get a Learning Path (AI Chat)

Not sure what to learn next? Use the [learning guide prompt](https://github.com/hollis-png/barlore/blob/main/prompts/learning_guide.md) — fill in your current state and the AI will tell you what to read, what to skip, and why.

It maps your concerns to specific Barlore entries across three layers:
- **Layer 1** — What should I do? (pick a program, learn movements, start tracking)
- **Layer 2** — Why does this work? (overload, nutrition, hypertrophy science)
- **Layer 3** — What's next? (testing, periodization, injury management)

## 4. llms.txt (For AI developers)

Point your agent to the structured index:

```
https://raw.githubusercontent.com/hollis-png/barlore/main/llms.txt
```

It includes:
- Query workflow for agents that can fetch URLs
- Goal-based program discovery via `goal_index.json`
- Links to all JSON indexes for structured search
- Crosscutting content URLs for nutrition, recovery, and injury prevention

## Available Data

| Resource | Count |
|----------|-------|
| Exercises | 688 (93 fully reviewed with research citations) |
| Programs | 53 (with structured `goals` field for query) |
| Training systems | 6 |
| Training principles | 11 |
| Nutrition & recovery docs | 22 |
| System guides | 12 |
| Goal categories | 6 (strength, hypertrophy, power, athletic performance, skill acquisition, general fitness) |

## Prompt Templates

| Template | Purpose | Link |
|----------|---------|------|
| Plan Generator | Get a personalized training plan | [plan_generator.md](https://github.com/hollis-png/barlore/blob/main/prompts/plan_generator.md) |
| Learning Guide | Get a personalized reading list | [learning_guide.md](https://github.com/hollis-png/barlore/blob/main/prompts/learning_guide.md) |
| Workout Log | Track your sessions | [workout_log.md](https://github.com/hollis-png/barlore/blob/main/prompts/workout_log.md) |
