export function appEnvPlugin() {
  return {
    name: "app-env-plugin",
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        if (req.url === "/__app-env") {
          res.setHeader("Content-Type", "application/json");
          res.end(JSON.stringify({ authEnabled: false }));
          return;
        }
        next();
      });
    },
  };
}
