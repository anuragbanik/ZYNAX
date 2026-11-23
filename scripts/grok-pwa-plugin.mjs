export function grokPwaPlugin() {
  return {
    name: "grok-pwa-plugin",
    transformIndexHtml(html) {
      return html;
    },
  };
}
