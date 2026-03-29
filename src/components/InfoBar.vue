<script setup>
defineProps({
  paramName: { type: String, default: '' },
  paramDescription: { type: String, default: '' },
  paramRange: { type: String, default: '' },
  isPerformance: { type: Boolean, default: false },
  hasInfo: { type: Boolean, default: false },
})
</script>

<template>
  <div
    class="mt-3 bg-bg/80 border rounded-lg px-4 py-2.5 min-h-[42px] flex items-center transition-all duration-200"
    :class="hasInfo ? 'border-accent/40' : 'border-white/10'"
  >
    <span class="text-accent font-bold text-xs uppercase tracking-wider mr-2">Param Info:</span>
    <template v-if="hasInfo">
      <span class="text-sm">
        <span class="text-white font-medium">{{ paramName }}</span>
        <template v-if="paramDescription"> — <span class="text-muted">{{ paramDescription }}</span></template>
        <span v-if="isPerformance" class="text-accent ml-1">[Performance]</span>
        <span v-if="paramRange" class="text-accent ml-2">[{{ paramRange }}]</span>
      </span>
    </template>
    <span v-else class="text-sm text-muted">Hover or click a parameter to see details...</span>
  </div>
</template>
