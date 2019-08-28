<template>
  <div>
    <div id="container" tabindex="0" style="width: 100%;height: 800px;"></div>
  </div>
</template>
<script>
import { get_company_map } from "@/service/api";

export default {
  data() {
    return {
      map: {}
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
    let responseData = await get_company_map();
    let markers = []
    for (var i = 0, marker; i < responseData.length; i++) {
      var marker = new AMap.Marker({
        map: this.map,
        position: responseData[i].lnglat,
        offset: new AMap.Pixel(-13, -30),
        title: responseData[i].name
      });
      markers.push(marker);
    }
  },
  methods: {}
};
</script>