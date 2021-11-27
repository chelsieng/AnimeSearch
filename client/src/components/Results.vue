<template>
  <div class="container mb-3">
    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
      <a href="/" class="mb-3 btn btn-light justify-content-end"><i class="bi bi-house-door-fill"></i> Home</a>

    </div>
    <div class="card">
      <div class="card-body">
        <div class="row mb-3 justify-content-between" v-for="r in this.$route.query.result" :key="r">
          <h3>{{ r['English Title'] }}</h3>
          <div class="col-lg-3">
            <img :src="r['Image_url']"
                 class="rounded" alt="">
          </div>
          <div class="col-lg-9">
            <h5>Description: </h5>
            <p>{{ r['description'] }}</p>
            <div class="row mb-3">
              <div class="col-4">
                <p class="card-text fw-bold"> Rating:
                  <span v-if="r['rating'] >= 6" class="text-success">{{ r['rating'] }}</span>
                  <span v-else class="text-danger">{{ r['rating'] }}</span></p>
              </div>
              <div class="col-4">
                <p class="card-text fw-bold">Popularity: <span class="fw-normal">{{ r['popularity'] }}</span></p>
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-4">
                <p class="card-text fw-bold">Duration:
                  <span v-if="r['duration_per_eps(min)'] === 0" class="fw-normal"> ? min/ep</span>
                  <span v-else class="fw-normal">{{ r['duration_per_eps(min)'] }} min/ep</span>
                </p>
              </div>
              <div class="col-4">
                <p class="card-text fw-bold">Number of episodes:
                  <span v-if="r['number_episodes'] === 'Unknown'" class="fw-normal"> ? </span>
                  <span v-else class="fw-normal">{{
                    r['number_episodes']
                  }}</span></p>
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-4">
                <p class="card-text fw-bold">Status: <span class="fw-normal">{{ r['Status'] }}</span></p>
              </div>
              <div class="col-4">
                <p class="card-text fw-bold">Source: <span class="fw-normal">{{ r['Source'] }}</span></p>
              </div>
            </div>
            <span class="fw-bold">Genre: </span><span v-for="i in r['genre'].length" :key="i" class="card-text">
                <span v-if="i === r['genre'].length">{{ r['genre'][i - 1] }}</span>
                <span v-else>{{ r['genre'][i - 1] }}, </span>
              </span>
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