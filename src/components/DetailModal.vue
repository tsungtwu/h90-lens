<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue'
import CategoryIcon from './CategoryIcon.vue'

const props = defineProps({
  algo: { type: Object, default: null },
})

const emit = defineEmits(['close'])
const copied = ref(false)
let copyTimeout = null

function copyLink() {
  navigator.clipboard.writeText(window.location.href).then(() => {
    copied.value = true
    clearTimeout(copyTimeout)
    copyTimeout = setTimeout(() => { copied.value = false }, 2000)
  })
}
const modalRef = ref(null)
let previousFocus = null

// Fix #5: Focus trap and ARIA
watch(() => props.algo, async (newVal) => {
  if (newVal) {
    previousFocus = document.activeElement
    await nextTick()
    modalRef.value?.focus()
    document.addEventListener('keydown', trapFocus)
  } else {
    document.removeEventListener('keydown', trapFocus)
    previousFocus?.focus()
    previousFocus = null
  }
})

onUnmounted(() => {
  document.removeEventListener('keydown', trapFocus)
  clearTimeout(copyTimeout)
})

function trapFocus(e) {
  if (e.key !== 'Tab' || !modalRef.value) return
  const focusable = modalRef.value.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  )
  if (focusable.length === 0) return
  const first = focusable[0]
  const last = focusable[focusable.length - 1]
  if (e.shiftKey) {
    if (document.activeElement === first) {
      e.preventDefault()
      last.focus()
    }
  } else {
    if (document.activeElement === last) {
      e.preventDefault()
      first.focus()
    }
  }
}

function onOverlayClick(e) {
  if (e.target === e.currentTarget) emit('close')
}
</script>

<template>
  <Teleport to="body">
    <div
      v-if="algo"
      role="dialog"
      aria-modal="true"
      :aria-label="`${algo.name} algorithm details`"
      class="fixed inset-0 z-[100] bg-black/70 backdrop-blur-sm flex items-center justify-center p-4"
      @click="onOverlayClick"
    >
      <div
        ref="modalRef"
        tabindex="-1"
        class="bg-bg-card border border-white/10 rounded-2xl max-w-2xl w-full max-h-[85vh] overflow-y-auto focus:outline-none"
        @click.stop
      >
        <div class="p-6">
          <!-- Header -->
          <div class="flex items-start justify-between mb-4">
            <div>
              <div class="flex items-center gap-2">
                <CategoryIcon :category="algo.category" class="w-6 h-6 text-accent" />
                <h2 class="font-heading text-2xl text-white italic uppercase">{{ algo.name }}</h2>
              </div>
              <p class="text-xs text-muted uppercase tracking-widest mt-1 ml-8">{{ algo.category }} // H90</p>
            </div>
            <div class="flex items-center gap-2">
              <button
                :aria-label="copied ? 'Link copied' : 'Copy link to this algorithm'"
                :class="[
                  'w-8 h-8 rounded-lg flex items-center justify-center transition-colors cursor-pointer',
                  copied ? 'bg-green-500/15 text-green-400' : 'text-muted hover:text-accent hover:bg-white/5'
                ]"
                @click="copyLink"
              >
                <svg v-if="!copied" xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
              </button>
              <button
                aria-label="Close dialog"
                class="text-muted hover:text-white transition-colors cursor-pointer text-2xl leading-none"
                @click="emit('close')"
              >
                &times;
              </button>
            </div>
          </div>

          <!-- Overview -->
          <p v-if="algo.overview" class="text-sm text-slate-300 mb-6 leading-relaxed">{{ algo.overview }}</p>

          <!-- All Parameters -->
          <h3 class="text-xs font-bold text-muted uppercase tracking-widest mb-3">All Parameters</h3>
          <div>
            <div
              v-for="(p, i) in algo.parameters"
              :key="p.name"
              class="py-3"
              :class="{ 'border-b border-white/5': i < algo.parameters.length - 1 }"
            >
              <div class="flex items-baseline gap-2 mb-1">
                <span class="text-white font-semibold text-sm">{{ p.name }}</span>
                <span v-if="p.range" class="text-accent text-xs font-medium">{{ p.range }}</span>
              </div>
              <p class="text-slate-300 text-sm leading-relaxed">{{ p.fullDescription || p.description || '' }}</p>
            </div>
          </div>

          <!-- Performance Parameters -->
          <template v-if="(algo.performanceParams || []).length > 0">
            <h3 class="text-xs font-bold text-muted uppercase tracking-widest mt-6 mb-3">Performance Parameters</h3>
            <div class="space-y-2">
              <div v-for="pp in algo.performanceParams" :key="pp.name" class="flex items-start gap-2">
                <span
                  class="px-3 py-1.5 rounded-full text-xs font-semibold bg-accent/15 text-accent border border-accent/30 shrink-0"
                >
                  {{ pp.name }}
                </span>
                <span v-if="pp.description" class="text-slate-400 text-xs pt-1">{{ pp.description }}</span>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </Teleport>
</template>
