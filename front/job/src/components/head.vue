<template>
   <div>
       <header class="navbar navbar-inverse navbar-static-top bs-docs-nav" id="top">
            <div class="container">
                <div class="navbar-header">
                    <button @click="show" aria-controls="bs-navbar" aria-expanded="false" class="navbar-toggle collapsed" data-target="#bs-navbar" data-toggle="collapse" type="button">
                        <span class="sr-only">
                            Toggle navigation
                        </span>
                        <span class="icon-bar">
                        </span>
                        <span class="icon-bar">
                        </span>
                        <span class="icon-bar">
                        </span>
                    </button>
                    <a class="navbar-brand" href="">
                        Logo
                    </a>
                </div>
                <nav class="collapse navbar-collapse" id="bs-navbar" v-bind:class="{ show: showNav }">
                    <ul class="nav navbar-nav">
                      
                        <li>
                            <router-link :to="{ name: 'weekline'}">一周职位统计</router-link>
                        </li>
                        <li>
                            <router-link :to="{ name: 'workyear'}">工作年限统计</router-link>
                           
                        </li>
                        <li>
                           <router-link :to="{ name: 'hot'}">热门公司统计</router-link>
                        </li>
                        <li>
                            <router-link :to="{ name: 'education'}">学历统计分析</router-link>
                        </li>
                        <li>
                           <router-link :to="{ name: 'wordcloud'}">技术词云图</router-link>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
   </div>
</template>

<style>
    .show{
        display: block;
    }
</style>
<script>
    export default {
        name: "menus",
        components: {},
        data(){
            return {
                showNav:false,
            }
        },
        methods:{
            show(){
                this.showNav = this.showNav == true ? false : true
               
            }
        },
        created() {
            
        },
        mounted() {
            
        },
    }
</script>