<template>
  <div>
    <div id="container" tabindex="0" style="width: 100%;height: 800px;margin-top: -20px"></div>
  </div>
</template>
<script>
import { get_company_map } from "@/service/api";

export default {
  data() {
    return {
      map: {},
      infoWindow:{}
    };
  },
  mounted() {
    /* eslint-disable */
    this.map = new AMap.Map("container", {
      resizeEnable: true,
      center: [121.472644, 31.217614],
      zoom: 13
    });
  },
  async created() {
    /* eslint-disable */
    let responseData = await get_company_map({ page: 1, page_size: 1000 });
    let markers = [];
    this.infoWindow = new AMap.InfoWindow({offset: new AMap.Pixel(0, -30)});
    for (var i = 0, marker; i < responseData.length; i++) {
      var marker = new AMap.Marker({
        map: this.map,
        position: [responseData[i].position_lng,responseData[i].position_lat],
        offset: new AMap.Pixel(-13, -30),
        title: responseData[i].company_name,
        extData:responseData[i]
      });
      marker.on('click', this.markerClick);
    }
  },
  methods: {
   markerClick(e){
    let content = this.createWindowInfo(e.target.getExtData())
    this.infoWindow.setContent(content);
    this.infoWindow.open(this.map, e.target.getPosition());
   },
   createWindowInfo(data){
     return `<div>
        <p>公司名称:<b>${data.company_name}</b></p>
        <p>公司人数:${data.company_scale}</p>
        <p>发展阶段:${data.company_stage}</p>
        <p>公司地址:${data.address}</p>
     </div`
   }

  }
};
</script>