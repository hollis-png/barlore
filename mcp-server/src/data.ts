import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const BARLORE_ROOT = join(__dirname, "..", "..");

function loadJSON<T>(relativePath: string): T {
  const raw = readFileSync(join(BARLORE_ROOT, relativePath), "utf-8");
  return JSON.parse(raw) as T;
}

function loadMarkdown(relativePath: string): string {
  return readFileSync(join(BARLORE_ROOT, relativePath), "utf-8");
}

export interface Muscle {
  id: string;
  role: "primary" | "secondary" | "stabilizer";
}

export interface Exercise {
  id: string;
  name: string;
  status: "complete" | "stub";
  aliases: string[];
  pattern: string[];
  muscles: Muscle[];
  equipment: string[];
  path: string;
  difficulty: {
    mobility_prerequisite: string | null;
    strength_prerequisite: string | null;
    technical_complexity: string | null;
  };
  variations: string[];
  alternatives: string[];
  muscle_activation_studies: unknown[];
  strength_curve: unknown;
  injury_risk: unknown;
}

export interface Program {
  id: string;
  name: string;
  system: string;
  level: string;
  periodization: string;
  exercise_refs: string[];
  path: string;
}

type ExerciseIndex = Record<string, Exercise>;
type MuscleIndex = Record<string, string[]>;
type ProgramIndex = Record<string, Program>;

let exercises: ExerciseIndex;
let muscleIndex: MuscleIndex;
let programs: ProgramIndex;

export function init() {
  exercises = loadJSON<ExerciseIndex>("index/exercises.json");
  muscleIndex = loadJSON<MuscleIndex>("index/muscle_index.json");
  programs = loadJSON<ProgramIndex>("index/programs.json");
}

export function getExercises(): ExerciseIndex {
  return exercises;
}

export function getMuscleIndex(): MuscleIndex {
  return muscleIndex;
}

export function getPrograms(): ProgramIndex {
  return programs;
}

export function getExerciseMarkdown(exercisePath: string): string {
  return loadMarkdown(exercisePath);
}

export function getCoreDocument(filename: string): string {
  return loadMarkdown(join("core", filename));
}

export function getSystemGuide(filename: string): string {
  return loadMarkdown(join("system_guides", filename));
}

export { BARLORE_ROOT };
