import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Front na 5174 (5173 ocupada por outro projeto). API FastAPI na 8077 (8000 ocupada).
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5174,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8077",
        changeOrigin: true,
      },
    },
  },
});
