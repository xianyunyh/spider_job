<template>
  <div id="app">
    <menus></menus>
    <router-view/>
  </div>
</template>
<script>
  import menus from '@/components/head'
  export default {
    components: {
      menus
    }
  }
</script>
