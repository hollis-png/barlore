#!/usr/bin/env python3
"""
Map Barlore exercise ids to free-exercise-db images (Public Domain / Unlicense).

Usage:
  python3 scripts/build_media_map.py

Writes site/.vitepress/theme/media_map.json. Images are not copied into this
repo; the site links to them on jsDelivr, pinned to FED_COMMIT.

Match order: manual override -> id/name/alias slug equals free-exercise-db name slug.
Exercises with no match are left out (the site shows no image for them).
"""
import json
import pathlib
import re
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / ".vitepress" / "theme" / "media_map.json"

FED_REPO = "yuhonas/free-exercise-db"
FED_COMMIT = "f00c92c7dcf1216a928a52c3706c7ce8e2f71ed5"
FED_JSON = f"https://raw.githubusercontent.com/{FED_REPO}/{FED_COMMIT}/dist/exercises.json"

# barlore id -> free-exercise-db exercise name. Hand-checked equivalents only;
# approximate movements (toes_to_bar, box_jumps, thrusters) are deliberately absent.
MANUAL = {
    "back_squat": "Barbell Full Squat",
    "overhead_press": "Standing Military Press",
    "bench_press": "Barbell Bench Press - Medium Grip",
    "conventional_deadlift": "Barbell Deadlift",
    "front_squat": "Front Barbell Squat",
    "rowing_ergometer": "Rowing, Stationary",
}


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def load_fed() -> dict:
    with urllib.request.urlopen(FED_JSON, timeout=30) as r:
        data = json.load(r)
    return {e["name"]: e for e in data}


def main() -> None:
    fed = load_fed()
    by_slug = {slug(n): e for n, e in fed.items()}

    result = {}
    for path in sorted((ROOT / "exercises").glob("*.md")):
        front = yaml.safe_load(path.read_text().split("---")[1])
        ex_id = front["id"]

        if ex_id in MANUAL:
            entry, how = fed[MANUAL[ex_id]], "manual"
        else:
            keys = [ex_id, slug(front["name"])] + [slug(a) for a in front.get("aliases") or []]
            entry = next((by_slug[k] for k in keys if k in by_slug), None)
            how = "exact"

        if entry and entry.get("images"):
            result[ex_id] = {"match": how, "name": entry["name"], "images": entry["images"]}

    OUT.write_text(json.dumps({"commit": FED_COMMIT, "map": result}, indent=1, ensure_ascii=False) + "\n")
    manual = sum(1 for v in result.values() if v["match"] == "manual")
    print(f"mapped {len(result)} exercises ({manual} manual) -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
