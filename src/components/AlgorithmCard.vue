<script setup>
import { ref, computed, watch } from 'vue'
import CategoryIcon from './CategoryIcon.vue'
import ParamCard from './ParamCard.vue'
import PerfCircle from './PerfCircle.vue'
import InfoBar from './InfoBar.vue'

const PARAMS_PER_PAGE = 10

const props = defineProps({
  algo: { type: Object, required: true },
})

const emit = defineEmits(['openDetail'])

const currentPage = ref(0)
const lockedParam = ref(null)
const hoveredParam = ref(null)

const totalPages = computed(() => Math.ceil(props.algo.parameters.length / PARAMS_PER_PAGE))

const pageParams = computed(() => {
  const start = currentPage.value * PARAMS_PER_PAGE
  return props.algo.parameters.slice(start, start + PARAMS_PER_PAGE)
})

// Fix #3: Reset lockedParam when page changes
watch(currentPage, () => {
  lockedParam.value = null
  hoveredParam.value = null
})

const activeParam = computed(() => lockedParam.value || hoveredParam.value)

const isActivePerf = computed(() => {
  const p = activeParam.value
  if (!p) return false
  return (props.algo.performanceParams || []).some((pp) => pp.name === p.name)
})

function onParamHover(param) {
  if (!lockedParam.value) hoveredParam.value = param
}

function onParamLeave() {
  if (!lockedParam.value) hoveredParam.value = null
}

function onParamLock(param) {
  if (lockedParam.value?.name === param.name) {
    lockedParam.value = null
    hoveredParam.value = null
  } else {
    lockedParam.value = param
  }
}
</script>

<template>
  <div class="bg-bg-card border border-white/10 rounded-2xl p-5 transition-all duration-200 hover:border-white/20 flex flex-col">
    <!-- Header -->
    <div class="flex items-start justify-between mb-1">
      <div>
        <div class="flex items-center gap-2">
          <CategoryIcon :category="algo.category" class="w-6 h-6 text-accent" />
          <h2 class="font-heading text-xl md:text-2xl text-white italic uppercase tracking-wide">
            {{ algo.name }}
          </h2>
        </div>
        <p class="text-xs text-muted uppercase tracking-widest mt-0.5 ml-8">{{ algo.category }} // H90</p>
      </div>
      <div class="flex items-center gap-2">
        <a
          v-if="algo.demoVideoId"
          :href="`https://www.youtube.com/watch?v=${algo.demoVideoId}`"
          target="_blank"
          rel="noopener"
          title="Sound Demo"
          aria-label="Watch sound demo on YouTube"
          class="w-7 h-7 rounded-full flex items-center justify-center transition-colors text-muted hover:text-red-500 hover:bg-white/5"
          @click.stop
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
        <button
          class="px-3 py-1.5 rounded-full border border-white/20 text-xs font-semibold text-white hover:border-accent hover:text-accent transition-all duration-200 cursor-pointer whitespace-nowrap"
          @click="emit('openDetail', algo.name)"
        >
          Detail &rarr;
        </button>
      </div>
    </div>

    <!-- Overview -->
    <p v-if="algo.overview" class="text-sm text-slate-400 leading-relaxed mt-2 mb-1">{{ algo.overview }}</p>

    <!-- Param Grid + Perf Params -->
    <div class="flex flex-col sm:flex-row items-stretch sm:items-start mt-4 gap-3">
      <div class="bg-bg/50 border border-white/5 rounded-xl p-3 flex-1 min-w-0">
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2">
          <ParamCard
            v-for="param in pageParams"
            :key="param.name"
            :param="param"
            :is-locked="lockedParam?.name === param.name"
            @hover="onParamHover"
            @leave="onParamLeave"
            @lock="onParamLock"
          />
        </div>
      </div>
      <!-- Performance Params -->
      <div v-if="(algo.performanceParams || []).length > 0" class="flex flex-row sm:flex-col items-center gap-2 flex-wrap justify-center">
        <PerfCircle
          v-for="pp in algo.performanceParams"
          :key="pp.name"
          :param="pp"
          :is-locked="lockedParam?.name === pp.name"
          @hover="onParamHover"
          @leave="onParamLeave"
          @lock="onParamLock"
        />
      </div>
    </div>

    <!-- Info Bar (pinned to bottom) -->
    <div class="mt-auto">
      <InfoBar
        :param-name="activeParam?.name || ''"
        :param-description="activeParam?.description || ''"
        :param-range="activeParam?.range || ''"
        :is-performance="isActivePerf"
        :has-info="!!activeParam"
      />
    </div>

    <!-- Page Buttons -->
    <div v-if="totalPages > 1" class="flex gap-2 mt-3">
      <button
        v-for="i in totalPages"
        :key="i"
        class="px-3 py-1 rounded-full text-xs font-semibold border border-white/15 cursor-pointer transition-all duration-200"
        :class="
          i - 1 === currentPage
            ? 'bg-accent text-bg'
            : 'text-muted hover:text-white'
        "
        @click="currentPage = i - 1"
      >
        PAGE {{ i }}
      </button>
    </div>
  </div>
</template>
