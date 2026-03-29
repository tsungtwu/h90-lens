<script setup>
defineProps({
  param: { type: Object, required: true },
  isLocked: { type: Boolean, default: false },
})

const emit = defineEmits(['hover', 'leave', 'lock'])
</script>

<template>
  <div
    class="param-card border rounded-lg p-3 cursor-pointer transition-all duration-200 relative group"
    :class="isLocked ? 'border-accent bg-accent/10' : 'border-white/10'"
    tabindex="0"
    role="button"
    :aria-label="`${param.name}: ${param.description}`"
    @mouseenter="emit('hover', param)"
    @mouseleave="emit('leave')"
    @click="emit('lock', param)"
    @keydown.enter.prevent="emit('lock', param)"
    @keydown.space.prevent="emit('lock', param)"
    @focus="emit('hover', param)"
    @blur="emit('leave')"
  >
    <div class="text-sm font-semibold text-white leading-tight">{{ param.name }}</div>

    <!-- Tooltip -->
    <div
      class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-52 bg-bg border border-accent/40 rounded-lg p-3 text-xs opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none z-10 shadow-lg shadow-black/50"
    >
      <div class="text-white font-medium mb-1">{{ param.name }}</div>
      <div class="text-slate-300 mb-1">{{ param.description }}</div>
      <div v-if="param.range" class="text-accent font-medium">{{ param.range }}</div>
      <div
        class="absolute top-full left-1/2 -translate-x-1/2 w-2 h-2 bg-bg border-r border-b border-accent/40 rotate-45 -mt-1"
      />
    </div>
  </div>
</template>
