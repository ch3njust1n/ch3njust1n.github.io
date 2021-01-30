<template>
	<div class="sect">
		<p>I am a dog dad, software engineer, independent machine learning researcher, entrepreneur, and traceur.</p>
		<p>My mind is currently exploring graph representation learning, hyperbolic deep learning, knowledge graphs, data fusion, and parkour theory.</p>
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