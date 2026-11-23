import { defineConfig } from 'astro/config';

// Wird später unter der eigenen Domain veröffentlicht.
export default defineConfig({
  site: 'https://radius56.de',
  trailingSlash: 'ignore',
});
