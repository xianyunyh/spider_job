<template>
<div class="container">
  <h2 class="text-center">最近一周职位发布趋势图</h2>
<ve-line :data="chartData" :settings="chartSettings"></ve-line>
</div>
</template>


<script>
import { get_week_line } from "@/service/api";
import VeLine from "v-charts/lib/line.common";
export default {
  components: { VeLine },
  data() {
    return {
      chartSettings: {
        labelMap: {
          date: "发布时间",
          count: "发布次数"
        }
      },
      chartData: {}
    };
  },
  created() {
    this.init();
  },
  methods: {
    async init() {
      let rows = await get_week_line();
      let columns = Object.keys(this.chartSettings["labelMap"]);
      this.chartData = { columns, rows };
    }
  }
};
</script>