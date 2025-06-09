// vite.config.js
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');

  return {
    plugins: [react()],
    define: {
      // Utilisé pour conditionner des blocs de code selon l'env
      __APP_ENV__: JSON.stringify(mode),

      // Injection explicite des variables d’environnement du frontend
      'import.meta.env.VITE_API_URL': JSON.stringify(env.VITE_API_URL),
      'import.meta.env.VITE_FRONT_VERSION': JSON.stringify(env.VITE_FRONT_VERSION),
    },
    build: {
      outDir: 'dist',
      sourcemap: true,
    },
    server: {
      port: 5173,
      strictPort: true,
    }
  };
});
