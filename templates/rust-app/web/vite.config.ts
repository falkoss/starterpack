// SPDX-License-Identifier: {{licence}}
// The web app is built into dist/, which the {{name}} binary embeds. In development, `pnpm dev` serves it and passes
// /api on to a `{{name}} serve` running on the usual port.
import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

export default defineConfig({
  plugins: [svelte()],
  build: { outDir: "dist", emptyOutDir: true, assetsInlineLimit: 0 },
  server: { proxy: { "/api": "http://127.0.0.1:{{api_port}}" } },
});
