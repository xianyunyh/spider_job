<template>

<div class="container">
  <div id="main">
    <wordcloud style="height:600px"
      :data="words"
      nameKey="name"
      valueKey="value">
      </wordcloud>
  </div>
</div>    
</template>

<style>
</style>

<script>
import {get_wordcloud} from '@/service/api'

import wordcloud from 'vue-wordcloud'
export default {
  components: {
    wordcloud
  },
  data() {
    return {
      words: []
    }
  },
   async created() {

     let res = await get_wordcloud()
     let data = []
     for (let t in res) {
       let tmp = {}
       tmp.name = t
       tmp.value = res[t]
       data.push(tmp)
     }
     this.words = data
  },
};
</script>