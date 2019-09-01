<template>
  <div class="container">
    <div id="main">
      <wordcloud style ="height:600px" :data="chartData.rows" nameKey="word" valueKey="count"></wordcloud>
    </div>
  </div>
</template>
<style>
</style>

<script>
import { get_wordcloud } from "@/service/api";
import wordcloud from 'vue-wordcloud'
export default {
  components: {
    wordcloud,
  },
  data() {
    this.chartSettings = {
        shape: 'circle',
        left:"left",
        sizeMin: 16,
        sizeMax: 100,
        rotationRange: [-90, 90],
        gridSize:100,
        width:"100%",
        height:"800px",
      }
    return {
      chartData: {
        columns: ["word", "count"],
        rows: [
        ]
      }
    };
  },
  async created() {
    let res = await get_wordcloud();
    let data = [];
    for (let t in res) {
      let tmp = {};
      tmp.word = t;
      tmp.count = res[t];
      data.push(tmp);
    }
    this.chartData.rows   =  data;
  }
};
</script>