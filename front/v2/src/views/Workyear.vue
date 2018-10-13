<template lang="">
    <div class="container">
        <h2 class="text-center">工作年限和薪资分析</h2>
         <ve-pie :data="chartData" :settings="pieSettings" :colors="colors"></ve-pie>
         <ve-histogram :data="salaryData"  :settings="salarySettings"></ve-histogram>
    </div>
    
</template>

<style scoped>
</style>

<script>
import VePie from "v-charts/lib/pie.common";
import VeHistogram from "v-charts/lib/histogram.common";
import { get_work_year } from "@/service/api";
export default {
  components: { VePie, VeHistogram },
  data() {
    return {
      colors: [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#91c7ae",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3"
      ],
      pieSettings: {
        labelMap: {
          work_year: "类型",
          count: "发布数"
        },
        yAxisType: ["normal"],
        dataType: function(v) {
          return v + "个";
        }
      },
      chartData: {
        columns: ["work_year", "count"],
        rows: []
      },
      salarySettings: {
        labelMap: {
          work_year: "工作年限",
          salary: "平均薪资"
        },
        digit: 0,
        xAxisType: "category"
      },
      salaryData: {
        columns: ["work_year", "salary"],
        rows: []
      }
    };
  },
  async created() {
    let response = await get_work_year();
    this.chartData.rows = response;
    this.salaryData.rows = response;
  }
};
</script>