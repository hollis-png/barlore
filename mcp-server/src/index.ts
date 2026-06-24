#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { createServer } from "node:http";
import { randomUUID } from "node:crypto";
import { init } from "./data.js";
import { toolDefinitions, handleTool } from "./tools.js";

function createMcpServer(): McpServer {
  const server = new McpServer({
    name: "barlore",
    version: "0.1.0",
  });

  for (const [name, def] of Object.entries(toolDefinitions)) {
    server.registerTool(
      name,
      {
        description: def.description,
        inputSchema: def.inputSchema,
      },
      async (args) => handleTool(name, args as Record<string, unknown>)
    );
  }

  return server;
}

init();

const useHttp = process.argv.includes("--http");
const port = parseInt(process.argv.find((a) => a.startsWith("--port="))?.split("=")[1] ?? "3100", 10);

if (useHttp) {
  const sessions = new Map<string, { server: McpServer; transport: StreamableHTTPServerTransport }>();

  const httpServer = createServer(async (req, res) => {
    const url = new URL(req.url ?? "/", `http://localhost:${port}`);

    if (url.pathname !== "/mcp") {
      res.writeHead(404, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Not found. Use /mcp endpoint." }));
      return;
    }

    const sessionId = req.headers["mcp-session-id"] as string | undefined;

    if (sessionId && sessions.has(sessionId)) {
      const session = sessions.get(sessionId)!;
      await session.transport.handleRequest(req, res);
      return;
    }

    if (req.method === "POST") {
      const transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: () => randomUUID(),
      });
      const server = createMcpServer();

      transport.onclose = () => {
        if (transport.sessionId) {
          sessions.delete(transport.sessionId);
        }
      };

      await server.connect(transport);
      await transport.handleRequest(req, res);

      if (transport.sessionId) {
        sessions.set(transport.sessionId, { server, transport });
      }
      return;
    }

    res.writeHead(400, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Bad request. Send POST to /mcp to initialize." }));
  });

  httpServer.listen(port, () => {
    console.error(`Barlore MCP Server (HTTP) listening on http://localhost:${port}/mcp`);
  });
} else {
  const server = createMcpServer();
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
