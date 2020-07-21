<template>
	<div class="sect">
		<h1>news</h1>
		<ul>
			<li class="item" v-for="(n, id) in news" :key="id">
				<span class="item-auth">{{ n.date }}</span>
				<p class="item-desc" v-html="n.desc"></p>
			</li>
		</ul>
	</div>
</template>

<script>
import updates from '@/json/news.json'

export default {
	name: 'projects',
	components: {
	},
	data() {
		return {
			news: updates
		}
	},
	methods: {

	}
}
</script>

<style scoped>
</style>