
<template>
<div class="container">
  <h2 class="text-center">每月发布职位趋势图</h2>
<ve-histogram :data="chartData" :settings="chartSettings"></ve-histogram>
<ve-line :data="chartData" :settings="chartSettings"></ve-line>
</div>
  
</template>

<script>
import { get_month_line } from "@/service/api";
import VeHistogram from "v-charts/lib/histogram.common";
import VeLine from "v-charts/lib/line.common";
export default {
  components: { VeHistogram,VeLine },
  data () {
    return {
      chartSettings:{
        labelMap: {
          date: "月份",
          count: "发布次数"
        }
    },
    chartData: {}
    }
  },
  created() {
    this.init();
  },
  methods: {
    async init() {
      let rows = await get_month_line();
      let columns = Object.keys(this.chartSettings["labelMap"]);
      this.chartData = { columns, rows };
    }
  }
}
</script>
