import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server:{ 
  proxy: {
    '^/(\_dash-component-suites|\_dash-dependencies|\_dash-layout|\_reload-hash|\_dash-update-component)': 'http://localhost:5000'
    },
   }
  
})
