<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body text-center">
            <form class="row g-3">
              <div>
                <h4 class="card-title text-danger">Oups, no results found!
                </h4>
              </div>
              <div>
                <a type="submit"
                   class="btn btn-outline-danger" href="javascript:history.back()">Back
                </a>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-sm-3"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Error"
}
</script>

<style scoped>

</style>