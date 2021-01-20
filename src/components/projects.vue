<template>
	<div class="sect">
		<h1>projects</h1>
		<ul>
			<li class="item" v-for="(p, id) in proj" :key="id">
				<span class="item-header">
					<a class="item-name" :href="p.href" target="_blank">
						{{ p.name }},
						<span class="item-year" v-if="p.year != null"> {{ p.year }}</span>
					</a>
				</span>
				<span class="item-venu" v-if="p.venu != null"> {{ p.venu }}</span>
				<span class="item-auth" v-if="p.auth != null">{{ p.auth }}</span>
				<p class="item-desc">{{ p.desc }}</p>
				<ul class="contact">
					<li class="link" v-for="(l, link_id) in p.links" :key="link_id">
						<a :href="l.href" target="_blank">{{ l.text }}</a>
					</li>
				</ul>
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
.contact {
    display: flex;
    flex-wrap: wrap;
}

.link {
	margin-top: 10px;
	font-size: 14px;
}

.link:not(:last-child) {
    margin-right: 1em;
}
</style>