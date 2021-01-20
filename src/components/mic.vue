<template>
	<div class="sect">
		<h1>entrepreneurship</h1>
		<ul>
			<li class="item" v-for="(i, id) in prog" :key="id">
				<span class="item-header">
					<span class="item-name">
						{{ i.name }},
					</span>
					<span class="item-year" v-if="i.year != null"> {{ i.year }}</span>
				</span>
				<p class="item-desc">{{ i.desc }}</p>
			</li>
		</ul>
	</div>
</template>

<script>
import entre from '@/json/entre.json'

export default {
	name: 'index',
	components: {
	},
	data() {
		return {
			prog: entre
		}
	},
	methods: {

	}
}
</script>

<style scoped>
.item {
	margin-bottom: 1em;
}

.item-name {
	display: inline;
}

.item-desc {
	margin-top: 5px;
}
</style>