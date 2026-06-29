<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'

const { frontmatter } = useData()

const TIER_CONFIG = {
  meta_analysis: { label: 'Meta-Analysis', abbr: 'MA', color: '#1a7f37', bg: '#dafbe1' },
  rct:           { label: 'RCT', abbr: 'RCT', color: '#0969da', bg: '#ddf4ff' },
  expert_consensus: { label: 'Expert Consensus', abbr: 'EC', color: '#6f42c1', bg: '#fbefff' },
  practitioner:  { label: 'Practitioner', abbr: 'P', color: '#9a6700', bg: '#fff8c5' },
  anecdotal:     { label: 'Anecdotal', abbr: 'A', color: '#656d76', bg: '#eaeef2' },
  literature_review: { label: 'Literature Review', abbr: 'LR', color: '#0969da', bg: '#ddf4ff' },
}

const TIER_ORDER = ['meta_analysis', 'rct', 'literature_review', 'expert_consensus', 'practitioner', 'anecdotal']

const tiers = computed(() => {
  const sources = frontmatter.value?.sources
  if (!Array.isArray(sources) || sources.length === 0) return []

  const seen = new Set()
  for (const s of sources) {
    const c = s?.credibility
    if (c && TIER_CONFIG[c]) seen.add(c)
  }

  return TIER_ORDER.filter(t => seen.has(t)).map(t => ({
    ...TIER_CONFIG[t],
    count: sources.filter(s => s?.credibility === t).length,
    key: t,
  }))
})

const category = computed(() => frontmatter.value?.category)
const status = computed(() => frontmatter.value?.status)

const showBadges = computed(() => {
  return tiers.value.length > 0 && ['exercise', 'principle', 'nutrition', 'recovery',
    'injury_prevention', 'cardio', 'special_populations', 'program'].includes(category.value)
})

const statusLabel = computed(() => {
  if (category.value !== 'exercise') return null
  const s = status.value
  if (s === 'complete') return { text: 'Reviewed', color: '#1a7f37', bg: '#dafbe1' }
  if (s === 'partial') return { text: 'Partial', color: '#9a6700', bg: '#fff8c5' }
  if (s === 'stub') return { text: 'Basic Info', color: '#656d76', bg: '#eaeef2' }
  return null
})
</script>

<template>
  <div v-if="showBadges || statusLabel" class="evidence-bar">
    <span v-if="statusLabel" class="evidence-badge" :style="{ color: statusLabel.color, backgroundColor: statusLabel.bg }">
      {{ statusLabel.text }}
    </span>
    <span class="evidence-sep" v-if="statusLabel && tiers.length > 0">·</span>
    <span v-if="tiers.length > 0" class="evidence-label">Sources:</span>
    <span
      v-for="tier in tiers"
      :key="tier.key"
      class="evidence-badge"
      :style="{ color: tier.color, backgroundColor: tier.bg }"
      :title="`${tier.count} ${tier.label} source${tier.count > 1 ? 's' : ''}`"
    >
      {{ tier.abbr }}
      <span v-if="tier.count > 1" class="evidence-count">×{{ tier.count }}</span>
    </span>
  </div>
</template>

<style scoped>
.evidence-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  margin: -8px 0 16px 0;
  font-size: 13px;
}

.evidence-label {
  color: var(--vp-c-text-3);
  font-size: 12px;
}

.evidence-sep {
  color: var(--vp-c-text-3);
}

.evidence-badge {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  line-height: 1.4;
  white-space: nowrap;
}

.evidence-count {
  font-weight: 400;
  opacity: 0.8;
}
</style>
