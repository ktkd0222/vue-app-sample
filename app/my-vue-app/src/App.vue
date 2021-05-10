<template>
    <global-header />
    <search-form />
    <main-content />
    <global-footer />
</template>

<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalFooter from '@/components/GlobalFooter.vue'
import SearchForm from '@/components/SearchForm.vue'
import MainContent from '@/components/MainContent.vue'

export default {
    components: {
        GlobalHeader,
        GlobalFooter,
        SearchForm,
        MainContent,
    }
}
</script>

<style lang="scss">
@import "bulma/bulma.sass";

</style>
