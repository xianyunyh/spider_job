<template>
<div class="container">
<ve-line :data="chartData" :settings="chartSettings" :colors="chartSettings.colors"></ve-line>
</div>
</template>


<script>
import {get_week_line} from '@/service/api'
import VeLine from 'v-charts/lib/line.common'
export default {
  components: { VeLine },
  data () {
    return {
        chartSettings:{
            labelMap: {
            'date': '日期',
            'count': '发布数'
            },
            yAxisType:["normal"],
            colors:['#c23531','#2f4554', '#61a0a8',
                    '#d48265', '#91c7ae','#749f83', 
                    '#ca8622', '#bda29a','#6e7074',
                    '#546570', '#c4ccd3']
        },
        chartData: {
            columns: ['date', 'count'],
            rows: [
            ]
        }
    }
  },
  async created() {
        let data =  await get_week_line()
        this.chartData.rows = data
  },
}
</script>