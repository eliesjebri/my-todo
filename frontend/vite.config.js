import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  // Chemin vers le dossier contenant les fichiers .env.frontend.*
  const envDir = path.resolve(__dirname, '../config')

  // Charge les variables d'environnement depuis config/.env.frontend.[mode]
  const env = loadEnv(mode, envDir, 'VITE_')

  return {
    plugins: [react()],
    envDir,
    define: {
      __APP_ENV__: JSON.stringify(mode),
    },
    server: {
      port: 3000,
      open: true,
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
    },
  }
})
