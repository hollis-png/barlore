# raw/ — Source Intake Layer

This directory stores **research notes and source records** before they are synthesized
into formal Barlore entries. It is the "raw materials" layer.

## What goes here

- Source URLs and DOIs
- Key facts extracted from papers (numbers, definitions, quotes)
- Credibility tier assessment
- Notes on what each source does and does not cover

## What does NOT go here

- Finished entry prose — that belongs in `core/`, `exercises/`, `programs/`, `crosscutting/`
- Opinions or personal notes without a source
- Anything that will end up directly in a Barlore entry

## Structure

```
raw/
  _template.md         ← copy this to start a new source file
  core/                ← source notes for core/ principles
  exercises/           ← source notes for exercises/ entries (EMG, ROM, technique)
  programs/            ← source notes for programs/ entries
  crosscutting/        ← source notes for nutrition/, recovery/ entries
```

## Relationship to the main entries

```
raw/core/volume_landmarks.md   →  synthesized into  →  core/volume_landmarks.md
raw/exercises/bench_press.md   →  synthesized into  →  exercises/bench_press.md
```

A `raw/` file should exist for every entry that required non-trivial source research.
Simple entries (1 obvious source, 1-2 facts) may be written directly without a raw file.

## Do not delete raw files after writing the entry

They serve as the audit trail: if someone questions a number in an entry,
the raw file shows exactly where it came from and what the original source said.
