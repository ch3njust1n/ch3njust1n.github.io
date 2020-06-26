<template>
	<div id="content">
		<ul class="contact">
			<li class="item" v-for="(i, id) in contact" :key="id">
				<a :href="i.href" target="_blank">{{ i.text }}</a>
			</li>
		</ul>
	</div>
</template>

<script>

export default {
	name: 'contact',
	components: {
	},
	data() {
		return {
			contact: [
				{'text': 'justinchen.io', 'href': '/'},
				{'text': 'linkedin', 'href': 'https://www.linkedin.com/in/justin-chen-776a63159/'},
				{'text': 'github', 'href': 'https://github.com/ch3njust1n'},
				{'text': 'medium', 'href': 'https://medium.com/@ch3njust1n'}
			]
		}
	},
	methods: {

	}
}
</script>

<style scoped>
.contact {
    display: flex;
}

.item:not(:last-child) {
    margin-right: 1em;
}
</style>