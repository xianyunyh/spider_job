<template>
   <div class="container">
        <table class="table table-bordered">
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
          <td><a :href="'http://www.zhipin.com/job/'+item.postion_id + '.html'">查看介绍</a></td>
        </tr>
       
      </tbody>
    </table>
   </div>
</template>
<style>
</style>

<script>
/* eslint-disable */
import { get_hot_compay } from "@/service/api";

export default {
  name: "hotcompany",
  components: {
    
  },
  data() {
    return {
        lists:[]
    }
  },

  methods: {
    async init() {
      let res = await get_hot_compay()
      this.lists = res
    }
  },
  created() {
    this.init();
  }
};
</script>