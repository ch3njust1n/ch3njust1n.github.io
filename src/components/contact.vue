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
import socials from '@/json/contacts.json'

export default {
	name: 'contact',
	components: {
	},
	data() {
		return {
			contact: socials
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