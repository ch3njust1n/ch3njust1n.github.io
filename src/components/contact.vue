<template>
	<div id="content" class="section">
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
				{'text': 'linkedin', 'href': 'https://www.linkedin.com/in/chenjus/'},
				{'text': 'github', 'href': 'https://github.com/ch3njust1n'},
				{'text': 'medium', 'href': 'https://medium.com/@ch3njust1n'},
				{'text': 'twitter', 'href': 'https://twitter.com/ch3njus'},
				{'text': 'soundcloud', 'href': 'https://soundcloud.com/ch3njust1n'},
				{'text': 'spotify', 'href': 'https://open.spotify.com/user/levelicarus?fbclid=IwAR2T5qDmJoklrw63X-JE096Y5TmouIezBPDG2SP7tIufo9rsSDNzFKejy7o'},
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
    flex-wrap: wrap;
    margin: 0 auto;
    padding: .5em auto;
}

.item:not(:last-child) {
    margin-right: 1em;
}
</style>