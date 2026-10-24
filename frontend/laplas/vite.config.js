import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    proxy: {
      "/api": {
        target: "http://46.253.132.225:7600",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
        // 👇 переписываем Domain из Set-Cookie на localhost,
        // чтобы браузер принял cookie от прокси
        cookieDomainRewrite: { "*": "localhost" },
        cookiePathRewrite: { "*": "/" },
        // 👇 чтобы видеть, что прокси реально работает
        configure: (proxy) => {
          proxy.on("proxyReq", (proxyReq, req) => {
            console.log("[proxy →]", req.method, req.url);
          });
          proxy.on("proxyRes", (proxyRes, req) => {
            console.log("[proxy ←]", proxyRes.statusCode, req.url);
            const sc = proxyRes.headers["set-cookie"];
            if (sc) console.log("[proxy cookie]", sc);
          });
          proxy.on("error", (err) => {
            console.error("[proxy error]", err.message);
          });
        },
      },
    },
  },
});