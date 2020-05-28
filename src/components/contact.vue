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
				{'text': 'linkedin', 'href': 'https://www.linkedin.com/in/justin-chen-776a63159/'},
				{'text': 'github', 'href': 'https://github.com/ch3njust1n'},
				{'text': 'twitter', 'href': 'https://twitter.com/ch3njus'}
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
    justify-content: center;

}

.item {
    margin-left: 1em;
}
</style>