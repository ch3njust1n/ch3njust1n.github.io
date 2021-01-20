<template>
	<div class="sect">
		<h1>news</h1>
		<ul>
			<li class="item" v-for="(n, id) in news" :key="id">
				<p class="item-desc">{{ n.date }} - {{ n.desc }}</p>
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