import { createServer } from "node:http";
import { readFileSync, existsSync, statSync } from "node:fs";
import { resolve, extname, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const distDir = resolve(__dirname, "../dist");

const MIME_TYPES = {
  ".html": "text/html",
  ".js": "text/javascript",
  ".mjs": "text/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
};

const port = process.env.PORT || 8080;
const host = "0.0.0.0";

const server = createServer((req, res) => {
  let reqPath = (req.url || "/").split("?")[0];
  if (reqPath === "/") reqPath = "/index.html";

  let filePath = resolve(distDir, "." + reqPath);
  if (!existsSync(filePath) || statSync(filePath).isDirectory()) {
    filePath = resolve(distDir, "index.html");
  }

  const ext = extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || "application/octet-stream";

  try {
    const content = readFileSync(filePath);
    res.writeHead(200, {
      "Content-Type": contentType,
      "Access-Control-Allow-Origin": "*"
    });
    res.end(content);
  } catch (err) {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not Found");
  }
});

server.listen(port, host, () => {
  console.log(`[ZYNAX Preview Server] Live at http://${host}:${port}`);
});
