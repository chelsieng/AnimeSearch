<template>
  <div id="app">
    <AnimeSearch msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import AnimeSearch from './components/AnimeSearch.vue'

export default {
  name: 'App',
  components: {
    AnimeSearch
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  /*color: #2c3e50;*/
  margin-top: 60px;
  /*margin-bottom: 0;*/
}

html {
  height: 100%;

}

body {
  /* Center and scale the image nicely */
  background: url("./assets/bg.jpg") no-repeat center;
  background-size: cover;
}
</style>
