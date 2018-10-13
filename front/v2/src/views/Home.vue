<template>
  <div>
    <ve-histogram :data="chartData"></ve-histogram>
    <ve-pie :data="chartData"></ve-pie>
  </div>
</template>

<script>
import VeHistogram from "v-charts/lib/histogram.common";
import VePie from "v-charts/lib/pie.common";
export default {
  components: { VeHistogram,VePie },
  data () {
    return {
      chartData: {
        columns: ['日期', '销售量'],
        rows: [
          { '日期': '1月1日', '销售量': 123 },
          { '日期': '1月2日', '销售量': 1223 },
          { '日期': '1月3日', '销售量': 2123 },
          { '日期': '1月4日', '销售量': 4123 },
          { '日期': '1月5日', '销售量': 3123 },
          { '日期': '1月6日', '销售量': 7123 }
        ]
      }
    }
  }
}
</script>