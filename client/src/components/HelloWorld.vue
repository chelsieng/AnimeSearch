<template>
  <div>
    <p>{{this.evaluate()}}</p>
    <p>{{ this.display }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:5000/"

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      display: ""
    }
  },
  methods: {
    async evaluate() {
      await axios
          .get(URL + "hello")
          .then((response) => {
            this.display = response.data
            console.log(response)
          })
          .catch((error) => {
            this.display = "Error"
            console.log(error)
          })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
