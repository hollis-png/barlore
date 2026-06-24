import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { WebStandardStreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/webStandardStreamableHttp.js";
import { z } from "zod";

import exercisesJson from "../data/exercises.json";
import muscleIndexJson from "../data/muscle_index.json";
import programsJson from "../data/programs.json";

const GITHUB_RAW =
  "https://raw.githubusercontent.com/hollis-png/barlore/main";

type Muscle = { id: string; role: "primary" | "secondary" | "stabilizer" };
type Exercise = {
  id: string;
  name: string;
  status: string;
  aliases: string[];
  pattern: string[];
  muscles: Muscle[];
  equipment: string[];
  path: string;
  variations: string[];
  alternatives: string[];
};
type Program = {
  id: string;
  name: string;
  system: string;
  level: string;
  periodization: string;
  exercise_refs: string[];
  path: string;
};

const exercises = exercisesJson as Record<string, Exercise>;
const muscleIndex = muscleIndexJson as Record<string, string[]>;
const programs = programsJson as Record<string, Program>;

async function fetchMarkdown(path: string): Promise<string> {
  const res = await fetch(`${GITHUB_RAW}/${path}`);
  if (!res.ok) return `File not available (${res.status})`;
  return res.text();
}

function text(content: string) {
  return { content: [{ type: "text" as const, text: content }] };
}

function createServer(): McpServer {
  const server = new McpServer({ name: "barlore", version: "0.1.0" });

  server.registerTool(
    "search_exercises",
    {
      description:
        "Search exercises by name, pattern, equipment, or muscle. Returns a summary list.",
      inputSchema: z.object({
        query: z.string().optional().describe("Fuzzy name search"),
        pattern: z.string().optional().describe("Movement pattern filter"),
        equipment: z.string().optional().describe("Equipment filter"),
        muscle: z
          .string()
          .optional()
          .describe("Muscle ID — only primary matches"),
        status: z.enum(["complete", "stub"]).optional(),
        limit: z.number().int().min(1).max(50).default(20),
      }),
    },
    async (args) => {
      let results = Object.values(exercises);
      const q = args.query?.toLowerCase();
      if (q)
        results = results.filter(
          (e) =>
            e.name.toLowerCase().includes(q) ||
            e.id.includes(q) ||
            e.aliases.some((a) => a.toLowerCase().includes(q))
        );
      if (args.pattern)
        results = results.filter((e) =>
          e.pattern.some((p) =>
            p.toLowerCase().includes(args.pattern!.toLowerCase())
          )
        );
      if (args.equipment)
        results = results.filter((e) =>
          e.equipment.some((eq) =>
            eq.toLowerCase().includes(args.equipment!.toLowerCase())
          )
        );
      if (args.muscle)
        results = results.filter((e) =>
          e.muscles.some((m) => m.id === args.muscle && m.role === "primary")
        );
      if (args.status) results = results.filter((e) => e.status === args.status);
      const limited = results.slice(0, args.limit);
      return text(
        JSON.stringify({
          total: results.length,
          returned: limited.length,
          exercises: limited.map((e) => ({
            id: e.id,
            name: e.name,
            status: e.status,
            pattern: e.pattern,
            equipment: e.equipment,
            primary_muscles: e.muscles
              .filter((m) => m.role === "primary")
              .map((m) => m.id),
          })),
        })
      );
    }
  );

  server.registerTool(
    "get_exercise",
    {
      description:
        "Get full markdown for an exercise by ID (EMG data, cues, sources).",
      inputSchema: z.object({ id: z.string() }),
    },
    async (args) => {
      const ex = exercises[args.id];
      if (!ex) {
        const suggestions = Object.keys(exercises)
          .filter((k) => k.includes(args.id) || args.id.includes(k))
          .slice(0, 5);
        return text(
          `Exercise "${args.id}" not found. Did you mean: ${suggestions.join(", ") || "(no suggestions)"}`
        );
      }
      return text(await fetchMarkdown(ex.path));
    }
  );

  server.registerTool(
    "search_by_muscle",
    {
      description:
        "Find exercises targeting a muscle, grouped by role (primary/secondary/stabilizer).",
      inputSchema: z.object({
        muscle_id: z.string(),
        role: z
          .enum(["primary", "secondary", "stabilizer", "any"])
          .default("any"),
      }),
    },
    async (args) => {
      const ids = muscleIndex[args.muscle_id];
      if (!ids) {
        return text(
          `Muscle "${args.muscle_id}" not found. Available: ${Object.keys(muscleIndex).sort().join(", ")}`
        );
      }
      const grouped: Record<string, string[]> = {
        primary: [],
        secondary: [],
        stabilizer: [],
      };
      for (const exId of ids) {
        const ex = exercises[exId];
        if (!ex) continue;
        for (const m of ex.muscles) {
          if (m.id === args.muscle_id) grouped[m.role]?.push(exId);
        }
      }
      if (args.role !== "any") {
        return text(
          JSON.stringify({
            muscle: args.muscle_id,
            role: args.role,
            count: grouped[args.role]?.length ?? 0,
            exercises: grouped[args.role] ?? [],
          })
        );
      }
      return text(JSON.stringify({ muscle: args.muscle_id, ...grouped, total: ids.length }));
    }
  );

  server.registerTool(
    "list_programs",
    {
      description: "List training programs, optionally filtered by system or level.",
      inputSchema: z.object({
        system: z.string().optional(),
        level: z.string().optional(),
      }),
    },
    async (args) => {
      let results = Object.values(programs);
      if (args.system)
        results = results.filter(
          (p) => p.system.toLowerCase() === args.system!.toLowerCase()
        );
      if (args.level)
        results = results.filter(
          (p) => p.level.toLowerCase() === args.level!.toLowerCase()
        );
      return text(
        JSON.stringify({
          total: results.length,
          programs: results.map((p) => ({
            id: p.id,
            name: p.name,
            system: p.system,
            level: p.level,
            periodization: p.periodization,
            exercise_count: p.exercise_refs.length,
          })),
        })
      );
    }
  );

  server.registerTool(
    "get_program",
    {
      description: "Get full markdown of a training program by ID.",
      inputSchema: z.object({ id: z.string() }),
    },
    async (args) => {
      const prog = programs[args.id];
      if (!prog) {
        const suggestions = Object.keys(programs)
          .filter((k) => k.includes(args.id))
          .slice(0, 5);
        return text(
          `Program "${args.id}" not found. Did you mean: ${suggestions.join(", ") || "(no suggestions)"}`
        );
      }
      return text(await fetchMarkdown(prog.path));
    }
  );

  server.registerTool(
    "get_training_concept",
    {
      description:
        "Read a core training science document (progressive_overload, periodization, sra_curve, volume_landmarks, rpe_rir, rep_continuum, specificity, deload).",
      inputSchema: z.object({
        concept: z.enum([
          "progressive_overload",
          "periodization",
          "sra_curve",
          "volume_landmarks",
          "rpe_rir",
          "rep_continuum",
          "specificity",
          "deload",
        ]),
      }),
    },
    async (args) => text(await fetchMarkdown(`core/${args.concept}.md`))
  );

  server.registerTool(
    "list_muscles",
    {
      description:
        "List all muscle IDs with exercise counts.",
      inputSchema: z.object({}),
    },
    async () => {
      const summary = Object.entries(muscleIndex)
        .map(([id, exs]) => ({ id, exercise_count: exs.length }))
        .sort((a, b) => b.exercise_count - a.exercise_count);
      return text(JSON.stringify({ total: summary.length, muscles: summary }));
    }
  );

  return server;
}

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/") {
      return new Response(
        JSON.stringify({
          name: "barlore-mcp",
          version: "0.1.0",
          description:
            "MCP server for the Barlore strength training knowledge base",
          endpoint: "/mcp",
          tools: [
            "search_exercises",
            "get_exercise",
            "search_by_muscle",
            "list_programs",
            "get_program",
            "get_training_concept",
            "list_muscles",
          ],
        }),
        { headers: { "Content-Type": "application/json" } }
      );
    }

    if (url.pathname !== "/mcp") {
      return new Response("Not found. Use /mcp", { status: 404 });
    }

    const server = createServer();
    const transport = new WebStandardStreamableHTTPServerTransport({
      sessionIdGenerator: undefined,
    });

    await server.connect(transport);
    return transport.handleRequest(request);
  },
};
