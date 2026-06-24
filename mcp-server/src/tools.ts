import { z } from "zod";
import {
  getExercises,
  getMuscleIndex,
  getPrograms,
  getExerciseMarkdown,
  getCoreDocument,
  getSystemGuide,
} from "./data.js";

export const toolDefinitions = {
  search_exercises: {
    description:
      "Search exercises by name, pattern, equipment, or muscle. Returns a summary list (not full markdown). Use get_exercise for full details.",
    inputSchema: z.object({
      query: z
        .string()
        .optional()
        .describe("Fuzzy name search (e.g. 'bench', 'curl')"),
      pattern: z
        .string()
        .optional()
        .describe(
          "Movement pattern filter: squat, hinge, horizontal press, vertical press, horizontal pull, vertical pull, carry, isolation"
        ),
      equipment: z
        .string()
        .optional()
        .describe(
          "Equipment filter: barbell, dumbbell, cable, machine, kettlebell, body only, bands, etc."
        ),
      muscle: z
        .string()
        .optional()
        .describe(
          "Muscle ID filter (e.g. biceps_brachii, pectoralis_major). Only returns exercises where this muscle is primary."
        ),
      status: z
        .enum(["complete", "stub"])
        .optional()
        .describe("Filter by data completeness"),
      limit: z
        .number()
        .int()
        .min(1)
        .max(50)
        .default(20)
        .describe("Max results (default 20)"),
    }),
  },

  get_exercise: {
    description:
      "Get full details for a specific exercise by ID. Returns the complete markdown with EMG data, cues, variations, and sources.",
    inputSchema: z.object({
      id: z
        .string()
        .describe(
          "Exercise ID (e.g. bench_press, back_squat, barbell_curl)"
        ),
    }),
  },

  search_by_muscle: {
    description:
      "Find all exercises that target a specific muscle. Returns exercise IDs grouped by role (primary/secondary/stabilizer).",
    inputSchema: z.object({
      muscle_id: z
        .string()
        .describe(
          "Muscle ID (e.g. biceps_brachii, deltoid_anterior, rectus_femoris)"
        ),
      role: z
        .enum(["primary", "secondary", "stabilizer", "any"])
        .default("any")
        .describe("Filter by muscle role"),
    }),
  },

  list_programs: {
    description:
      "List all training programs, optionally filtered by system or level.",
    inputSchema: z.object({
      system: z
        .string()
        .optional()
        .describe(
          "Training system: powerlifting, bodybuilding, olympic, strongman, crossfit, calisthenics"
        ),
      level: z
        .string()
        .optional()
        .describe("Level: beginner, intermediate, advanced"),
    }),
  },

  get_program: {
    description:
      "Get full details of a training program by ID. Returns the complete markdown.",
    inputSchema: z.object({
      id: z.string().describe("Program ID (e.g. 5_3_1, phat, starting_strength)"),
    }),
  },

  get_training_concept: {
    description:
      "Read a core training science document: progressive_overload, periodization, sra_curve, volume_landmarks, rpe_rir, rep_continuum, specificity, deload.",
    inputSchema: z.object({
      concept: z
        .enum([
          "progressive_overload",
          "periodization",
          "sra_curve",
          "volume_landmarks",
          "rpe_rir",
          "rep_continuum",
          "specificity",
          "deload",
        ])
        .describe("Training concept name"),
    }),
  },

  list_muscles: {
    description:
      "List all muscle IDs in the knowledge base with the count of exercises targeting each.",
    inputSchema: z.object({}),
  },
};

export function handleTool(
  name: string,
  args: Record<string, unknown>
): { content: Array<{ type: "text"; text: string }> } {
  switch (name) {
    case "search_exercises":
      return searchExercises(args);
    case "get_exercise":
      return getExercise(args);
    case "search_by_muscle":
      return searchByMuscle(args);
    case "list_programs":
      return listPrograms(args);
    case "get_program":
      return getProgram(args);
    case "get_training_concept":
      return getTrainingConcept(args);
    case "list_muscles":
      return listMuscles();
    default:
      return text(`Unknown tool: ${name}`);
  }
}

function text(content: string) {
  return { content: [{ type: "text" as const, text: content }] };
}

function searchExercises(args: Record<string, unknown>) {
  const exercises = getExercises();
  const query = (args.query as string | undefined)?.toLowerCase();
  const pattern = (args.pattern as string | undefined)?.toLowerCase();
  const equipment = (args.equipment as string | undefined)?.toLowerCase();
  const muscle = args.muscle as string | undefined;
  const status = args.status as string | undefined;
  const limit = (args.limit as number) || 20;

  let results = Object.values(exercises);

  if (query) {
    results = results.filter(
      (e) =>
        e.name.toLowerCase().includes(query) ||
        e.id.includes(query) ||
        e.aliases.some((a) => a.toLowerCase().includes(query))
    );
  }

  if (pattern) {
    results = results.filter((e) =>
      e.pattern.some((p) => p.toLowerCase().includes(pattern))
    );
  }

  if (equipment) {
    results = results.filter((e) =>
      e.equipment.some((eq) => eq.toLowerCase().includes(equipment))
    );
  }

  if (muscle) {
    results = results.filter((e) =>
      e.muscles.some((m) => m.id === muscle && m.role === "primary")
    );
  }

  if (status) {
    results = results.filter((e) => e.status === status);
  }

  const limited = results.slice(0, limit);

  const summary = limited.map((e) => ({
    id: e.id,
    name: e.name,
    status: e.status,
    pattern: e.pattern,
    equipment: e.equipment,
    primary_muscles: e.muscles
      .filter((m) => m.role === "primary")
      .map((m) => m.id),
  }));

  return text(
    JSON.stringify(
      { total: results.length, returned: limited.length, exercises: summary },
      null,
      2
    )
  );
}

function getExercise(args: Record<string, unknown>) {
  const id = args.id as string;
  const exercises = getExercises();
  const exercise = exercises[id];

  if (!exercise) {
    const suggestions = Object.keys(exercises)
      .filter((k) => k.includes(id) || id.includes(k))
      .slice(0, 5);
    return text(
      `Exercise "${id}" not found. Did you mean: ${suggestions.join(", ") || "(no suggestions)"}`
    );
  }

  try {
    const markdown = getExerciseMarkdown(exercise.path);
    return text(markdown);
  } catch {
    return text(
      JSON.stringify(
        { ...exercise, note: "Full markdown not available, showing index data" },
        null,
        2
      )
    );
  }
}

function searchByMuscle(args: Record<string, unknown>) {
  const muscleId = args.muscle_id as string;
  const role = (args.role as string) || "any";
  const muscleIdx = getMuscleIndex();
  const exercises = getExercises();

  const fromIndex = muscleIdx[muscleId];
  if (!fromIndex) {
    const available = Object.keys(muscleIdx).sort();
    return text(
      `Muscle "${muscleId}" not found. Available: ${available.join(", ")}`
    );
  }

  const grouped: Record<string, string[]> = {
    primary: [],
    secondary: [],
    stabilizer: [],
  };

  for (const exId of fromIndex) {
    const ex = exercises[exId];
    if (!ex) continue;
    for (const m of ex.muscles) {
      if (m.id === muscleId) {
        grouped[m.role]?.push(exId);
      }
    }
  }

  if (role !== "any") {
    return text(
      JSON.stringify(
        {
          muscle: muscleId,
          role,
          count: grouped[role]?.length ?? 0,
          exercises: grouped[role] ?? [],
        },
        null,
        2
      )
    );
  }

  return text(
    JSON.stringify(
      {
        muscle: muscleId,
        primary: grouped.primary,
        secondary: grouped.secondary,
        stabilizer: grouped.stabilizer,
        total: fromIndex.length,
      },
      null,
      2
    )
  );
}

function listPrograms(args: Record<string, unknown>) {
  const system = args.system as string | undefined;
  const level = args.level as string | undefined;
  const programs = getPrograms();

  let results = Object.values(programs);

  if (system) {
    results = results.filter(
      (p) => p.system.toLowerCase() === system.toLowerCase()
    );
  }
  if (level) {
    results = results.filter(
      (p) => p.level.toLowerCase() === level.toLowerCase()
    );
  }

  const summary = results.map((p) => ({
    id: p.id,
    name: p.name,
    system: p.system,
    level: p.level,
    periodization: p.periodization,
    exercise_count: p.exercise_refs.length,
  }));

  return text(JSON.stringify({ total: results.length, programs: summary }, null, 2));
}

function getProgram(args: Record<string, unknown>) {
  const id = args.id as string;
  const programs = getPrograms();
  const program = programs[id];

  if (!program) {
    const suggestions = Object.keys(programs)
      .filter((k) => k.includes(id))
      .slice(0, 5);
    return text(
      `Program "${id}" not found. Did you mean: ${suggestions.join(", ") || "(no suggestions)"}`
    );
  }

  try {
    const markdown = getExerciseMarkdown(program.path);
    return text(markdown);
  } catch {
    return text(JSON.stringify(program, null, 2));
  }
}

function getTrainingConcept(args: Record<string, unknown>) {
  const concept = args.concept as string;
  try {
    const content = getCoreDocument(`${concept}.md`);
    return text(content);
  } catch {
    return text(`Concept document "${concept}" not found.`);
  }
}

function listMuscles() {
  const muscleIdx = getMuscleIndex();
  const summary = Object.entries(muscleIdx)
    .map(([id, exercises]) => ({ id, exercise_count: exercises.length }))
    .sort((a, b) => b.exercise_count - a.exercise_count);

  return text(JSON.stringify({ total: summary.length, muscles: summary }, null, 2));
}
