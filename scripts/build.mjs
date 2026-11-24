import { mkdirSync, cpSync, copyFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = resolve(__dirname, "..");
const distDir = resolve(rootDir, "dist");

console.log("[ZYNAX Build] Starting production deployment build for ZYNAX...");
console.log(`[ZYNAX Build] Root: ${rootDir}`);
console.log(`[ZYNAX Build] Dist: ${distDir}`);

// 1. Ensure dist directory exists
mkdirSync(distDir, { recursive: true });

// 2. Copy index.html
const indexHtml = resolve(rootDir, "index.html");
if (existsSync(indexHtml)) {
  copyFileSync(indexHtml, resolve(distDir, "index.html"));
  console.log("✓ Copied index.html -> dist/index.html");
} else {
  console.error("❌ Error: index.html not found in root!");
  process.exit(1);
}

// 3. Copy public directory contents to dist
const publicDir = resolve(rootDir, "public");
if (existsSync(publicDir)) {
  cpSync(publicDir, distDir, { recursive: true });
  console.log("✓ Copied public/ assets -> dist/");
}

// 4. Copy solutions directory to dist/solutions (for VS Code template launcher)
const solutionsDir = resolve(rootDir, "solutions");
if (existsSync(solutionsDir)) {
  const distSolutions = resolve(distDir, "solutions");
  mkdirSync(distSolutions, { recursive: true });
  cpSync(solutionsDir, distSolutions, { recursive: true });
  console.log("✓ Copied solutions/ -> dist/solutions/");
}

// 5. Copy presentation file if present
const presFile = resolve(rootDir, "zynax-presentation.pptx");
if (existsSync(presFile)) {
  copyFileSync(presFile, resolve(distDir, "zynax-presentation.pptx"));
  console.log("✓ Copied zynax-presentation.pptx -> dist/zynax-presentation.pptx");
}

console.log("[ZYNAX Build] Production build completed successfully in dist/!");
