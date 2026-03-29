<script setup>
defineProps({
  param: { type: Object, required: true },
  isLocked: { type: Boolean, default: false },
})

const emit = defineEmits(['hover', 'leave', 'lock'])
</script>

<template>
  <div
    class="perf-circle w-14 h-14 rounded-full border-2 flex flex-col items-center justify-center cursor-pointer relative group"
    :class="isLocked ? 'border-accent bg-accent/10' : 'border-white/20'"
    tabindex="0"
    role="button"
    :aria-label="`${param.name}: ${param.description || 'Performance parameter'}`"
    @mouseenter="emit('hover', param)"
    @mouseleave="emit('leave')"
    @click="emit('lock', param)"
    @keydown.enter.prevent="emit('lock', param)"
    @keydown.space.prevent="emit('lock', param)"
    @focus="emit('hover', param)"
    @blur="emit('leave')"
  >
    <span class="text-accent font-bold text-sm">{{ param.name[0] }}</span>
    <span class="text-[8px] text-muted uppercase tracking-wider mt-0.5">{{ param.name }}</span>
  </div>
</template>
