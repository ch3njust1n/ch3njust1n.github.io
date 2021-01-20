<template>
	<div class="sect">
		<h1>parkour theory</h1>
		<ul class="links">
			<li class="item" v-for="(i, id) in links" :key="id">
				<a :href="i.href" target="_blank">{{ i.text }}</a>
			</li>
		</ul>
	</div>
</template>

<script>
	import socials from '@/json/parkourtheory.json'

export default {
	name: 'parkourtheory',
	components: {
	},
	data() {
		return {
			links: socials
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
    margin: 0 auto;
    padding: .5em auto;
}

.item:not(:last-child) {
    margin-right: 1em;
}
</style>