<template>
    <div>

    <highcharts :options="options"></highcharts>
    </div>
</template>

<style>
</style>

<script>
/* eslint-disable */
export default {
  name: "chartline",
  props: [ "series", "xAxis"],
  data() {
    return {
      options: {
        chart: {
            type: 'spline',
        },
        xAxis: {
          categories: []
        },
        yAxis: { title: { text: "" }, },
        legend: {
          layout: "vertical",
          align: "right",
          verticalAlign: "middle"
        },
        series: [],
        responsive: {
          rules: [
            {
              condition: { maxWidth: 500 },
              chartOptions: {
                legend: {
                  layout: "horizontal",
                  align: "center",
                  verticalAlign: "bottom"
                }
              }
            }
          ]
        },
        credits: {
          enabled: false // 禁用版权信息
        }
      }
    };
  },
  watch:{
    xAxis(newvalue,old){
      console.log(newvalue)
    }
  },
  created() {
  console.log(this.$props)
   this.options.series = this.$props.series
   this.options.xAxis  = this.$props.xAxis
  },
  methods: {},
  mounted() {
    
  }
};
</script>