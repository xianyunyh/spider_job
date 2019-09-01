<template>
  <div class="container">
    <h2 class="text-center">公司行业和规模比例</h2>
    <div class="row">
      <div class="col-lg-4 col-md-6 col-sm-12"><ve-pie :title="chartTitle" :data="chartData" :legend="legend"></ve-pie></div>
      <div class="col-lg-4 col-md-6 col-sm-12"><ve-pie :title="stageTitle" :data="companyStageData" :legend="legend"></ve-pie></div>
      <div class="col-lg-4 col-md-6 col-sm-12"><ve-pie :title="areaTitle" :data="companyAreaData" :legend="legend"></ve-pie></div>
    </div>
    <table style="margin-top:20px" class="table table-bordered">
      <caption style="font-size:24px" class="text-center" align="center">热门公司列表</caption>
      <thead>
        
        <tr>
          <th class="text-center">公司名称</th>
          <th>发布次数</th>
          <th>薪资范围</th>
          <th>职位地址</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in lists" :key="item.postion_id">
          <td>{{item.company_name}}</td>
          <td>{{item.count}}</td>
          <td>{{item.salary.min}}-{{item.salary.max}}</td>
          <td><a target="_blank" :href="'http://www.zhipin.com/gongsi/'+item.company_id + '.html'">查看介绍</a></td>
        </tr>
       
      </tbody>
    </table>
        
  </div>
</template>

<script>
import { get_company_analysis,get_hot_compay } from "@/service/api";
import VePie from "v-charts/lib/pie.common";
import "echarts/lib/component/title";
export default {
  components: { VePie },
  data() {
    this.chartTitle = {
      text: "公司规模",
      x:"center"
    };
    this.stageTitle ={
        text: "公司发展情况",
        x:"center"
    }
    this.areaTitle ={
        text: "公司行业比例",
        x:"center"
    }
    this.legend =  {
        y : 'bottom'
    }
    return {
      lists:[],
      chartData: {
        columns: ["_id", "total"],
        rows: []
      },
      companyAreaData: {
        columns: ["_id", "total"],
        rows: []
      },
      companyStageData:{
        columns: ["_id", "total"],
        rows: []
      }
    };
  },
  mounted() {},
  async created() {
    this.chartData.rows= await get_company_analysis();
    this.companyStageData.rows = await get_company_analysis({"group":"company_stage"});
    let company_area_data = await get_company_analysis({"group":"company_area"});
    company_area_data = company_area_data.filter(item=>item.total >= 5);
    this.companyAreaData.rows = company_area_data;
    let res = await get_hot_compay();
    this.lists = res.filter(item=>item.count > 10)
  },
  methods: {}
};
</script>