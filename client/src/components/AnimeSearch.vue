<template>
  <div class="container">
    <!--    <form>-->
    <div class="input-group input-group-lg mb-3">
      <span class="input-group-text"><i class="bi bi-search"></i></span>
      <input @keyup.enter="search()" ref="keyword" type="text" class="form-control" placeholder="Enter keyword">
    </div>
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Advanced Search</h5>
        <div class="row">
          <div class="col-sm-4 p-4">
            <div class="row gap-3">
              <select ref="status" class="form-select" aria-label="Default select example">
                <option selected>Status</option>
                <option value="Finished Airing"> Finished Airing</option>
                <option value="Currently Airing"> Currently Airing</option>
              </select>
              <!--              <select class="form-select" aria-label="Default select example">-->
              <!--                <option selected class="bg-transparent">Duration</option>-->
              <!--                <option value=" duration <= 5 "> less than 5 min</option>-->
              <!--                <option value=" duration > 5 and duration < 10 "> 5 min ~ 10 min</option>-->
              <!--                <option value=" duration >= 10 and duration < 30 "> 10 min ~ 30 min</option>-->
              <!--                <option value=" duration >= 30 and duration < 60  "> 30 min ~ 1 hour+</option>-->
              <!--                <option value=" duration >= 60 and duration < 120 "> 1 hour ~ 2 hour+</option>-->
              <!--                <option value=" duration >= 120 and duration < 180 "> 2 hour ~ 3 hour+</option>-->
              <!--                <option value=" duration >= 180 "> 3 hour+</option>-->
              <!--              </select>-->
            </div>
          </div>
          <div class="col-sm-4 p-4">
            <div class="row gap-3">
              <select ref="genre" class="form-select" aria-label="Default select example">
                <option selected>Genre</option>
                <option value="Action">Action</option>
                <option value="Comedy">Comedy</option>
                <option value="Adventure">Adventure</option>
                <option value="Drama">Drama</option>
                <option value="Harem">Harem</option>
                <option value="Slice of Life">Slice of Life</option>
                <option value="Sci-Fi">Sci-Fi</option>
                <option value="Fantasy">Fantasy</option>
                <option value="Music">Music</option>
                <option value="Kids">Kids</option>
                <option value="School">School</option>
                <option value="Mystery">Mystery</option>
                <option value="Romance">Romance</option>
                <option value="Ecchi">Ecchi</option>
                <option value="Historical">Historical</option>
                <option value="Sports">Sports</option>
                <option value="Horror">Horror</option>
                <option value="Military">Military</option>
              </select>
              <!--              <select class="form-select" aria-label="Default select example">-->
              <!--                <option selected>Number of episodes</option>-->
              <!--                <option value=" episodes < 5 ">less than 5</option>-->
              <!--                <option value=" episodes < 10 ">less than 10</option>-->
              <!--                <option value=" episodes >= 10 and episodes < 15 ">10 ~ 15</option>-->
              <!--                <option value=" episodes >= 15 and episodes < 25 ">15 ~ 25</option>-->
              <!--                <option value=" episodes >= 25 and episodes < 35 ">25 ~ 35</option>-->
              <!--                <option value=" episodes >= 35 and episodes < 100 ">35 ~ 100</option>-->
              <!--                <option value=" episodes >= 100 and episodes < 200 ">100 ~ 200</option>-->
              <!--                <option value=" episodes >= 200 and episodes < 300 ">200 ~ 300</option>-->
              <!--                <option value=" episodes >= 300 and episodes < 400 ">300 ~ 400</option>-->
              <!--                <option value=" episodes >= 400 and episodes < 500 ">400 ~ 500</option>-->
              <!--                <option value=" episodes >= 500 ">500+</option>-->
              <!--              </select>-->
              <!--              <select class="form-select" aria-label="Default select example">-->
              <!--                <option selected>Aired on</option>-->
              <!--                <option value="2021">2021</option>-->
              <!--                <option value="2020">2020</option>-->
              <!--                <option value="2019">2019</option>-->
              <!--                <option value="2018">2018</option>-->
              <!--                <option value="2017">2017</option>-->
              <!--                <option value="2016">2016</option>-->
              <!--                <option value="2015">2015</option>-->
              <!--                <option value="2014">2014</option>-->
              <!--                <option value="2013">2013</option>-->
              <!--                <option value="2012">2012</option>-->
              <!--                <option value="2011">2011</option>-->
              <!--                <option value="2010">2010</option>-->
              <!--                <option value="2009">2009</option>-->
              <!--                <option value="2008">2008</option>-->
              <!--                <option value="2007">2007</option>-->
              <!--                <option value="2006">2006</option>-->
              <!--                <option value="2005">2005</option>-->
              <!--                <option value="2004">2004</option>-->
              <!--                <option value="2003">2003</option>-->
              <!--                <option value="2002">2002</option>-->
              <!--                <option value="2001">2001</option>-->
              <!--                <option value="2000">2000</option>-->
              <!--                <option value="<2000">&lt;2000</option>-->
              <!--              </select>-->
            </div>
          </div>
          <div class="col-sm-4 p-4">
            <div class="row gap-3">
              <select ref="source" class="form-select" aria-label="Default select example">
                <option selected>Source</option>
                <option value="Manga">Manga</option>
                <option value="Original">Original</option>
                <option value="Visual novel">Visual Novel</option>
                <option value="Light novel">Light novel</option>
                <option value="Game">Game</option>
                <option value="Novel">Novel</option>
                <option value="4-koma Manga">4-koma Manga</option>
                <option value="Book">Book</option>
                <option value="Music">Music</option>
                <option value="Picture Book">Picture Book</option>
                <option value="Web Manga">Web Manga</option>
                <option value="Card Game">Card Game</option>
                <option value="Radio">Radio</option>
                <option value="Other">Other</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-4 p-4">
        <div class="row gap-3">
        </div>
      </div>
      <div class="col-sm-4 p-4">
        <div class="row gap-3">
          <input type="button" @click="search()" value="Search" class="btn btn-light btn-block">
        </div>
      </div>
      <div class="col-sm-4 p-4">
        <div class="row gap-3">
        </div>
      </div>
    </div>
    <!--    </form>-->


  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:5000/"

export default {
  name: 'AnimeSearch',
  data() {
    return {
      display: "",
    }
  },
  methods: {
    async advancedSearch() {
      await axios
          .get(URL + "advanced_search/" + this.$refs.keyword.value, {
            params: {
              "Status": this.$refs.status.value,
              "genre": this.$refs.genre.value,
              "Source": this.$refs.source.value
            }
          })
          .then((response) => {
            if (response.data.length === 0) {
              throw onerror;
            } else {
              this.$router.push({path: "results", query: {result: response.data}})
            }
          })
          .catch((error) => {
            console.log(error)
            this.$router.push({path: "error"})
          })
    },
    async search() {
      if (this.$refs.status.value !== "Status" || this.$refs.genre.value !== "Genre" || this.$refs.source.value !== "Source") {
        await this.advancedSearch();
      } else {
        await axios
            .get(URL + "search/" + this.$refs.keyword.value)
            .then((response) => {
              if (response.data.length === 0) {
                throw onerror;
              } else {
                this.$router.push({path: "results", query: {result: response.data}})
              }
            })
            .catch((error) => {
              console.log(error)
              this.$router.push({path: "error"})
            })
      }

    },
  }
}
</script>

<!--Add "scoped" attribute to limit CSS to this component only-->
<!--<style scoped>-->

<!--</style>-->
