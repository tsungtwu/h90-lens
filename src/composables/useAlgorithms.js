import { ref, computed } from 'vue'

const allAlgorithms = ref([])
const searchQuery = ref('')
const activeCategories = ref(new Set())
const isLoaded = ref(false)
const loadError = ref(null)
let isLoading = false

const categories = computed(() => {
  return [...new Set(allAlgorithms.value.map((a) => a.category))].sort()
})

// Fix #12: Pre-compute category counts as data instead of passing function prop
const categoryCounts = computed(() => {
  const counts = {}
  for (const algo of allAlgorithms.value) {
    counts[algo.category] = (counts[algo.category] || 0) + 1
  }
  return counts
})

const filteredAlgorithms = computed(() => {
  const query = searchQuery.value.toLowerCase()
  return allAlgorithms.value.filter((algo) => {
    if (activeCategories.value.size > 0 && !activeCategories.value.has(algo.category)) {
      return false
    }
    if (query) {
      const nameMatch = algo.name.toLowerCase().includes(query)
      const paramMatch = algo.parameters.some((p) => p.name.toLowerCase().includes(query))
      // Fix #2: null safety for overview
      const overviewMatch = (algo.overview || '').toLowerCase().includes(query)
      if (!nameMatch && !paramMatch && !overviewMatch) return false
    }
    return true
  })
})

export function useAlgorithms() {
  async function loadAlgorithms() {
    // Fix #6: Guard against double-call
    if (isLoading || isLoaded.value) return
    isLoading = true
    loadError.value = null
    try {
      const res = await fetch(`${import.meta.env.BASE_URL}data/algorithms.json`)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      allAlgorithms.value = await res.json()
      isLoaded.value = true
    } catch (e) {
      // Fix #13: User-friendly error message
      loadError.value = 'Unable to load algorithm data. Please refresh the page and try again.'
      console.error('Failed to load algorithms.json:', e)
    } finally {
      isLoading = false
    }
  }

  function setSearch(query) {
    searchQuery.value = query
  }

  function toggleCategory(category) {
    const cats = new Set(activeCategories.value)
    if (cats.has(category)) {
      cats.delete(category)
    } else {
      cats.add(category)
    }
    activeCategories.value = cats
  }

  function getAlgorithmByName(name) {
    return allAlgorithms.value.find((a) => a.name === name)
  }

  function toSlug(name) {
    return name.toLowerCase().replace(/\s+/g, '-')
  }

  function getAlgorithmBySlug(slug) {
    return allAlgorithms.value.find((a) => toSlug(a.name) === slug)
  }

  return {
    allAlgorithms,
    filteredAlgorithms,
    categories,
    categoryCounts,
    activeCategories,
    searchQuery,
    isLoaded,
    loadError,
    loadAlgorithms,
    setSearch,
    toggleCategory,
    getAlgorithmByName,
    toSlug,
    getAlgorithmBySlug,
  }
}
