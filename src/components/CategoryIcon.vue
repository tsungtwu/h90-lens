<script setup>
import { computed, useAttrs } from 'vue'
import { useCategoryIcons } from '../composables/useCategoryIcons'

defineOptions({ inheritAttrs: false })

const props = defineProps({
  category: { type: String, required: true },
})

const attrs = useAttrs()
const { getIconSvg } = useCategoryIcons()

const svgHtml = computed(() => {
  const svg = getIconSvg(props.category)
  if (!svg) return ''
  const classes = attrs.class || ''
  return svg.replace('<svg ', `<svg class="${classes}" `)
})
</script>

<template>
  <span v-if="svgHtml" v-html="svgHtml" />
</template>
