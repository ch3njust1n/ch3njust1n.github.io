<template>
	<div class="sect">
		<h1>open-source</h1>
		<ul>
			<li class="item" v-for="(p, id) in proj" :key="id">
				<span class="item-header">
					<a class="item-name" :href="p.href" target="_blank">
						{{ p.name }}
						<span class="item-year" v-if="p.year != null">, {{ p.year }}</span>
					</a>
				</span>
				<p class="item-desc">{{ p.desc }}</p>
			</li>
		</ul>
	</div>
</template>

<script>
import projects from '@/json/projects.json'

export default {
	name: 'projects',
	components: {
	},
	data() {
		return {
			proj: projects
		}
	},
	methods: {

	}
}
</script>

<style scoped>
</style>