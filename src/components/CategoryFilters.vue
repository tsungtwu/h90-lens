<script setup>
import CategoryIcon from './CategoryIcon.vue'

defineProps({
  categories: { type: Array, required: true },
  activeCategories: { type: Set, required: true },
  categoryCounts: { type: Object, required: true },
})

const emit = defineEmits(['toggle'])
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <button
      v-for="cat in categories"
      :key="cat"
      class="filter-btn flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-medium border border-white/15 text-muted hover:border-accent hover:text-white transition-all duration-200 cursor-pointer"
      :class="{ 'active !bg-accent !text-bg !border-accent': activeCategories.has(cat) }"
      @click="emit('toggle', cat)"
    >
      <CategoryIcon :category="cat" class="w-4 h-4" />
      {{ cat }}
      <span class="text-xs opacity-60">{{ categoryCounts[cat] || 0 }}</span>
    </button>
  </div>
</template>
