import { defineConfig } from 'vite';
import svelte from '@sveltejs/vite-plugin-svelte';

// https://vitejs.dev/config/
export default defineConfig({
	server: {
		proxy: {
			'/generate': 'http://localhost:5174'
		}
	},
	build: {
		outDir: './public' // Output directory for static files
	}
});
