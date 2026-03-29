<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useAlgorithms } from './composables/useAlgorithms'
import SearchBar from './components/SearchBar.vue'
import CategoryFilters from './components/CategoryFilters.vue'
import AlgorithmCard from './components/AlgorithmCard.vue'
import DetailModal from './components/DetailModal.vue'

const {
  filteredAlgorithms,
  categories,
  categoryCounts,
  activeCategories,
  isLoaded,
  loadError,
  loadAlgorithms,
  setSearch,
  toggleDemoOnly,
  demoOnly,
  toggleCategory,
  getAlgorithmByName,
  toSlug,
  getAlgorithmBySlug,
} = useAlgorithms()

const searchBar = ref(null)
const detailAlgo = ref(null)

function openDetail(name) {
  const algo = getAlgorithmByName(name)
  if (!algo) return
  detailAlgo.value = algo
  window.location.hash = `algo=${toSlug(algo.name)}`
}

function closeDetail() {
  detailAlgo.value = null
  history.replaceState(null, '', window.location.pathname + window.location.search)
}

function openDetailFromHash() {
  const hash = window.location.hash
  const match = hash.match(/^#algo=(.+)$/)
  if (!match) return
  const algo = getAlgorithmBySlug(decodeURIComponent(match[1]))
  if (algo) {
    detailAlgo.value = algo
  } else {
    history.replaceState(null, '', window.location.pathname + window.location.search)
  }
}

function onKeydown(e) {
  if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
    e.preventDefault()
    searchBar.value?.focus()
  }
  if (e.key === 'Escape') {
    if (detailAlgo.value) {
      closeDetail()
      return
    }
    searchBar.value?.focus()
  }
}

onMounted(async () => {
  await loadAlgorithms()
  openDetailFromHash()
  window.addEventListener('hashchange', openDetailFromHash)
  document.addEventListener('keydown', onKeydown)
})

onUnmounted(() => {
  window.removeEventListener('hashchange', openDetailFromHash)
  document.removeEventListener('keydown', onKeydown)
})
</script>

<template>
  <!-- Header -->
  <header class="sticky top-0 z-50 bg-bg/90 backdrop-blur-md border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 md:px-6 lg:px-8 py-4">
      <div class="flex items-center justify-between mb-4">
        <h1 class="font-heading text-2xl md:text-3xl text-white tracking-wide">H90 Lens</h1>
        <span class="text-xs text-muted">Firmware 1.12.5</span>
      </div>
      <SearchBar ref="searchBar" @update:search="setSearch" />
      <div class="flex items-center gap-3">
        <CategoryFilters
          class="flex-1 min-w-0"
          :categories="categories"
          :active-categories="activeCategories"
          :category-counts="categoryCounts"
          @toggle="toggleCategory"
        />
        <button
          class="filter-btn flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-medium border border-white/15 text-muted hover:border-accent hover:text-white transition-all duration-200 cursor-pointer shrink-0"
          :class="{ '!bg-red-500/20 !text-red-400 !border-red-500/50': demoOnly }"
          @click="toggleDemoOnly"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Demo
        </button>
      </div>
    </div>
  </header>

  <!-- Result Count -->
  <div class="max-w-7xl mx-auto px-4 md:px-6 lg:px-8 pt-4 pb-2">
    <p v-if="filteredAlgorithms.length > 0" class="text-sm text-muted">
      {{ filteredAlgorithms.length }} algorithm{{ filteredAlgorithms.length !== 1 ? 's' : '' }}
    </p>
  </div>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-4 md:px-6 lg:px-8 pb-12">
    <!-- Loading -->
    <div v-if="!isLoaded && !loadError" class="text-center py-20">
      <p class="text-muted">Loading algorithms...</p>
    </div>

    <!-- Error -->
    <div v-else-if="loadError" class="text-center py-20">
      <p class="text-xl text-red-400 mb-2">{{ loadError }}</p>
    </div>

    <!-- Cards -->
    <template v-else>
      <div v-if="filteredAlgorithms.length > 0" class="grid grid-cols-1 xl:grid-cols-2 gap-6">
        <AlgorithmCard
          v-for="algo in filteredAlgorithms"
          :key="algo.name"
          :algo="algo"
          @open-detail="openDetail"
        />
      </div>

      <!-- No Results -->
      <div v-else class="text-center py-20">
        <p class="text-xl text-muted mb-2">No matching algorithms found</p>
        <p class="text-sm text-muted/60">Try a different search term or clear your filters</p>
      </div>
    </template>
  </main>

  <!-- Footer -->
  <footer class="border-t border-white/10 py-6 text-center text-xs text-muted/60">
    <p>
      H90 Lens — Quick reference for
      <a
        href="https://www.eventideaudio.com/h90"
        target="_blank"
        rel="noopener"
        class="underline hover:text-muted transition-colors"
      >
        Eventide H90
      </a>
      algorithms
    </p>
    <p class="mt-1">Data sourced from H90 Manual v1.12.5. Not affiliated with Eventide Audio.</p>
  </footer>

  <!-- Detail Modal -->
  <DetailModal :algo="detailAlgo" @close="closeDetail" />
</template>
