<template>
	<div class="sect">
		<p>I am a software engineer, independent machine learning researcher and entrepreneur.</p>
		<p>My mind is currently exploring graph representation learning, knowledge graphs, differential geometry, democratizing machine intelligence education, and parkour theory.</p>
	</div>
</template>

<script>

export default {
	name: 'index',
	components: {
	},
	data() {
		return {

		}
	},
	methods: {

	}
}
</script>

<style scoped>
#content {
    margin: 1em 0;
}

.sect {
	display: flex;
	justify-content: space-between;
	flex-direction: column;
}

.sect p {
	font-size: 14px;
	margin-bottom: 1em;
}

.sect p a {
	display: inline;
	text-decoration: underline;
}
</style>