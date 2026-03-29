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
  toggleCategory,
  getAlgorithmByName,
} = useAlgorithms()

const searchBar = ref(null)
const detailAlgo = ref(null)

function openDetail(name) {
  detailAlgo.value = getAlgorithmByName(name)
}

function closeDetail() {
  detailAlgo.value = null
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

onMounted(() => {
  loadAlgorithms()
  document.addEventListener('keydown', onKeydown)
})

onUnmounted(() => {
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
      <CategoryFilters
        :categories="categories"
        :active-categories="activeCategories"
        :category-counts="categoryCounts"
        @toggle="toggleCategory"
      />
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
