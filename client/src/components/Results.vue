<template>
  <div class="container mb-3">
    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
      <a href="/" class="mb-3 btn btn-light justify-content-end"><i class="bi bi-house-door-fill"></i> Home</a>

    </div>
    <div class="card">
      <div class="card-body">
        <div class="row mb-3 justify-content-between" v-for="r in this.$route.query.result" :key="r">
          <h5>{{ r['English Title'] }}</h5>
          <div class="col-lg-3">
            <img :src="r['Image_url']"
                 class="rounded" alt="">
          </div>
          <div class="col-lg-9">
            <p class="card-text">Description: {{ r['description'] }}</p>
            <p class="card-title"> Rating: {{ r['rating'] }}</p>
            <p class="card-text">Number of episodes: {{ r['number_episodes'] }}</p>
            <p class="card-text">Duration: {{ r['duration_per_eps(min)'] }}</p>
            <p class="card-text">Popularity: {{ r['popularity'] }}</p>
            <p class="card-text">Status: {{ r['Status'] }}</p>
            <p class="card-text">Source: {{ r['Source'] }}</p>
            <span>Genre: </span><span v-for="g in r['genre']" :key="g" class="card-text"> {{ g }} </span>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

export default {
  name: "Results",
}

</script>

<style scoped>

</style>