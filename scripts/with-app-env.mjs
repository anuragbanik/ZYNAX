import { spawn } from "node:child_process";

const args = process.argv.slice(2);
if (args.length === 0) {
  process.exit(0);
}

const child = spawn(args[0], args.slice(1), {
  stdio: "inherit",
  shell: true,
  env: {
    ...process.env,
    VITE_AUTH_ENABLED: process.env.VITE_AUTH_ENABLED || "false",
  },
});

child.on("exit", (code) => {
  process.exit(code ?? 0);
});
