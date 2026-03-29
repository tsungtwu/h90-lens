<script setup>
import { ref, onUnmounted } from 'vue'

const emit = defineEmits(['update:search'])
const input = ref(null)
let timeout = null

function onInput(e) {
  clearTimeout(timeout)
  timeout = setTimeout(() => {
    emit('update:search', e.target.value)
  }, 150)
}

// Fix #10: Clear timeout on unmount
onUnmounted(() => {
  clearTimeout(timeout)
})

function focus() {
  input.value?.focus()
}

defineExpose({ focus })
</script>

<template>
  <div class="relative mb-4">
    <svg
      class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-muted"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
      />
    </svg>
    <input
      ref="input"
      type="text"
      placeholder="Search algorithms or parameters... ( / )"
      class="w-full pl-10 pr-4 py-3 bg-primary/50 border border-white/10 rounded-xl text-slate-100 placeholder-muted focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-colors"
      @input="onInput"
    />
  </div>
</template>
