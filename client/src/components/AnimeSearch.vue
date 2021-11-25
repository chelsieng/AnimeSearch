<template>
  <div class="container">
    <form>
      <div class="input-group input-group-lg mb-3">
        <span class="input-group-text"><i class="bi bi-search"></i></span>
        <input type="text" class="form-control" placeholder="Enter keyword" aria-label="Username">
      </div>
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Advanced Search</h5>
          <div class="row">
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
                <select class="form-select" aria-label="Default select example">
                  <option selected>Status</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>

                <select class="form-select" aria-label="Default select example">
                  <option selected class="bg-transparent">Duration</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
              </div>
            </div>
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
                <select class="form-select" aria-label="Default select example">
                  <option selected>Number of episodes</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
                <select class="form-select" aria-label="Default select example">
                  <option selected>Aired on</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
              </div>
            </div>
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
                <select class="form-select" aria-label="Default select example">
                  <option selected>Genre</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
                <select class="form-select" aria-label="Default select example">
                  <option selected>Source</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
              </div>
            </div>
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
              </div>
            </div>
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
                <a href="" class="btn btn-outline-dark btn-block"> Search </a>
              </div>
            </div>
            <div class="col-sm-4 p-4">
              <div class="row gap-3">
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
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
      display: "",
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

 Add "scoped" attribute to limit CSS to this component only
<!--<style scoped>-->

<!--</style>-->
