<template>
  <section class="hero is-medium">
    <div class="hero-body has-text-centered">
      <h1 class="title is-2">{{ message }}</h1>
      <div id="hero-input-group" class="field has-addons has-addons-centered">
        <div class="control">
          <input class="input is-medium" type="text" placeholder="Search..." />
        </div>
        <div class="control">
          <a class="button is-medium is-primary">
            <i class="fal fa-search"></i>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { axios } from '@/plugins/axios/index'

export default {
    components: {
    },
    data() {
      return {
        message : ''
      }
    },
    mounted() {
      this.get_hello().then((response) =>{
        this.message = response.data.message
      })
    },
    methods: {
      get_hello() {
        return axios.get('api/hello')
      }
    },
}
</script>
<style lang="scss" scoped>

</style>