<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import mediaMap from './media_map.json'

const { frontmatter } = useData()

const CDN = 'https://cdn.jsdelivr.net/gh/yuhonas/free-exercise-db'

const entry = computed(() => {
  if (frontmatter.value?.category !== 'exercise') return null
  return mediaMap.map[frontmatter.value?.id] ?? null
})

const frames = computed(() => {
  if (!entry.value) return []
  const labels = ['Start', 'End']
  return entry.value.images.slice(0, 2).map((p, i) => ({
    src: `${CDN}@${mediaMap.commit}/exercises/${p}`,
    label: labels[i],
  }))
})
</script>

<template>
  <figure v-if="entry" class="exercise-media">
    <div class="exercise-media-frames">
      <div v-for="f in frames" :key="f.src" class="exercise-media-frame">
        <img :src="f.src" :alt="`${entry.name} — ${f.label}`" loading="lazy" decoding="async" />
        <span>{{ f.label }}</span>
      </div>
    </div>
    <figcaption>
      Images: <a href="https://github.com/yuhonas/free-exercise-db" target="_blank" rel="noopener">free-exercise-db</a>
      (public domain) — “{{ entry.name }}”
    </figcaption>
  </figure>
</template>

<style scoped>
.exercise-media {
  margin: 0 0 1.25rem;
}
.exercise-media-frames {
  display: flex;
  gap: 0.75rem;
}
.exercise-media-frame {
  position: relative;
  flex: 1 1 0;
  max-width: 280px;
}
.exercise-media-frame img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}
.exercise-media-frame span {
  position: absolute;
  left: 6px;
  bottom: 6px;
  padding: 1px 7px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  border-radius: 3px;
}
.exercise-media figcaption {
  margin-top: 0.4rem;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
</style>
