import { spawn } from "node:child_process";

const action = process.argv[2] || "start";
console.log(`[preview] Action: ${action}`);

if (action === "restart" || action === "start") {
  const child = spawn("npx", ["vite", "preview", "--port", "8081", "--host", "0.0.0.0"], {
    stdio: "inherit",
    shell: true,
  });
  child.on("exit", (code) => process.exit(code ?? 0));
} else {
  process.exit(0);
}
