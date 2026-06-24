# Barlore — Strength & Physique Training Encyclopedia

A comprehensive training knowledge base covering six major training systems, 680 exercises, 52 named programs, and shared nutrition and recovery knowledge. Designed to help you find the right program, understand every movement, and train smarter.

## What Can I Do With This?

### Get a Personalized Training Plan

Open [`prompts/plan_generator.md`](prompts/plan_generator.md), fill in your profile (goal, experience, equipment, schedule), and paste the entire file into any AI chatbot (ChatGPT, Claude, Gemini, etc.). It will recommend a program and generate a weekly schedule tailored to you — including exercise substitutions if you have injuries or limited equipment.

### Browse Training Systems

Each system has a philosophy page explaining what it is, who it's for, and how it differs from the others:

| System | Focus | Example Programs |
|--------|-------|------------------|
| [Powerlifting](systems/powerlifting/index.md) | Maximal strength in squat, bench, deadlift | Starting Strength, 5/3/1, Westside Conjugate |
| [Bodybuilding](systems/bodybuilding/index.md) | Muscle size and aesthetics | PPL, PHUL, PHAT, German Volume Training |
| [Olympic Weightlifting](systems/olympic/index.md) | Explosive power — snatch and clean & jerk | Catalyst Athletics, Pendlay, Bulgarian Method |
| [Calisthenics](systems/calisthenics/index.md) | Bodyweight strength and skills | BWF Recommended Routine, Overcoming Gravity, Convict Conditioning |
| [Strongman](systems/strongman/index.md) | Odd-object strength and carry events | Starting Strongman, Cube Method, Brian Shaw's Split |
| [CrossFit](systems/crossfit/index.md) | General fitness across all domains | CrossFit Foundations, CompTrain, HWPO |

### Look Up Any Exercise

The `exercises/` folder has 680 entries. Each complete entry includes:
- What muscles it works (and how much, backed by research when available)
- Step-by-step execution cues
- Injury risks and who should avoid it
- Variations, progressions, and alternatives

### Learn Training Fundamentals

The `core/` folder covers principles every lifter should know:
- Progressive overload, periodization, deload strategies
- RPE and RIR (rating effort), the rep continuum
- SRA curves (when to train a muscle again)
- Volume landmarks (how much training is enough vs. too much)

### Nutrition & Recovery Basics

The `crosscutting/` folder has shared knowledge that applies across all systems:
- Protein, carb, and fat requirements
- Nutrient timing and supplementation
- Sleep, warm-up, active recovery, and deload protocols
- Injury prevention and mobility
- Guidance for athletes over 35 and female-specific considerations

---

## Current Coverage

| Category | Count | Status |
|----------|-------|--------|
| Exercises | 680 total | 92 complete with full detail, 588 with basic info |
| Programs | 52 | Covering all 6 systems across beginner to advanced |
| Training principles | 8 | Complete |
| Nutrition & recovery | 20 | Complete |
| System philosophies | 6 | Complete |

---

## How It's Organized

```
exercises/       680 movement entries (what each exercise IS)
programs/        52 named training programs (how to train)
systems/         6 training philosophies (why each system works)
core/            Fundamental training principles
crosscutting/    Nutrition, recovery, injury prevention
prompts/         AI prompt templates (start here!)
```

The key idea: **exercises are neutral**. The back squat isn't "a powerlifting exercise" — it's a movement that powerlifting, bodybuilding, and CrossFit all use differently. Each program describes how it uses each exercise, with its own technique cues and rep schemes.

---

## MCP Server — Let AI Agents Query Barlore

Barlore has a built-in [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server, so AI agents like Claude Code, Cursor, and Windsurf can search exercises, programs, and training science directly.

### Cloud (Recommended)

Already deployed, no setup needed:

```jsonc
// Add to your AI tool's MCP settings (e.g. Claude Code settings.json)
{
  "mcpServers": {
    "barlore": {
      "type": "streamable-http",
      "url": "https://barlore-mcp.hollisyen210.workers.dev/mcp"
    }
  }
}
```

### Local (stdio)

```bash
cd mcp-server && npm install
npm start
```

```jsonc
// Claude Code settings.json
{
  "mcpServers": {
    "barlore": {
      "command": "npx",
      "args": ["tsx", "/path/to/Barlore/mcp-server/src/index.ts"]
    }
  }
}
```

### Available Tools

| Tool | Description |
|------|-------------|
| `search_exercises` | Search by name, pattern, equipment, or muscle |
| `get_exercise` | Full exercise detail (EMG data, cues, sources) |
| `search_by_muscle` | Find exercises targeting a specific muscle |
| `list_programs` | Browse programs by system or level |
| `get_program` | Full program detail |
| `get_training_concept` | Training science docs (periodization, SRA, RPE, etc.) |
| `list_muscles` | All muscle IDs with exercise counts |

---

## For Developers

### Building the Index

The `index/` folder contains auto-generated JSON files used by the plan generator and search tools. To rebuild:

```bash
pip install pyyaml
python3 scripts/build_index.py
```

### Useful Scripts

| Script | What it does |
|--------|-------------|
| `scripts/build_index.py` | Regenerates `index/` and checks data integrity |
| `scripts/coverage.py` | Shows what's complete and what's missing |
| `scripts/stub_audit.py` | Checks if any programs reference incomplete exercises |
| `scripts/build_plan_matrix.py` | Regenerates the programs table for the plan generator prompt |

### Data Format

Entries use YAML front matter in Markdown files. See [`SCHEMA.md`](SCHEMA.md) for the full field specification and [`glossary.md`](glossary.md) for canonical naming.

### Contributing

Exercise entries progress through stages: **stub** (basic info from import) → **complete** (full muscle data, execution cues, injury risk, research citations). To upgrade a stub, follow the format of any complete entry (e.g., `exercises/bench_press.md`) and run `build_index.py` to validate.
