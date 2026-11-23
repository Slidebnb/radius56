// Lädt alle Beiträge aus src/content/posts/*.md – neuester zuerst.
const files = import.meta.glob('../content/posts/*.md', { eager: true });

export const KATEGORIEN = [
  { slug: 'news', name: 'News' },
  { slug: 'events', name: 'Events' },
  { slug: 'blaulicht', name: 'Blaulicht' },
  { slug: 'geld-alltag', name: 'Geld & Alltag' },
  { slug: 'mitmachen', name: 'Mitmachen' },
  { slug: 'immo', name: 'Immo' },
];

export function kategorieName(slug) {
  return KATEGORIEN.find((k) => k.slug === slug)?.name ?? slug;
}

export function getPosts() {
  return Object.entries(files)
    .map(([path, mod]) => ({
      slug: path.split('/').pop().replace(/\.md$/, ''),
      ...mod.frontmatter,
      Content: mod.Content,
    }))
    .sort((a, b) => new Date(b.date) - new Date(a.date));
}

export function formatDatum(iso) {
  return new Date(iso).toLocaleDateString('de-DE', { day: 'numeric', month: 'long', year: 'numeric' });
}
