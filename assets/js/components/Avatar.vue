<template>
  <span class="v-avatar" :style="styleSize" :aria-label="alt">
    <span class="v-avatar-text" v-text="name" :style="{background: bg, color: fg}"></span>
  </span>
</template>

<script>
import wc from 'word-color'

export default {
  props: ['alt', 'size'],

  data() {
    return {}
  },

  computed: {
    bg() {
      if (!this.alt) {
        return 'black'
      }
      return wc(this.alt)
    },

    fg() {
      if (!this.alt) {
        return 'black'
      }
      var bg = wc.rgb(this.alt)
      if ((bg[0] * 299 + bg[1] * 587 + bg[2] * 144) > 200000) {
        return 'black'
      }
      return 'white'
    },

    name() {
      if (!this.alt) {
        return ''
      }
      return this.alt.charAt(0).toUpperCase()
    },

    styleSize() {
      if (!this.size) return

      var px = this.size + 'px'
      return {
        'width': px,
        'height': px,
        'line-height': px,
        'font-size': this.size / 2 + 'px'
      }
    }
  },
}
</script>

<style>
.v-avatar {
  display: inline-block;
  text-align: center;
  vertical-align: middle;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  overflow: hidden;
  font: 300 normal 24px/48px sans-serif;
}

.v-avatar--squared {
  border-radius: 2px;
}

.v-avatar .v-avatar-text {
  display: inline-block;
  width: 100%;
  height: 100%;
 user-select: none;
}
</style>