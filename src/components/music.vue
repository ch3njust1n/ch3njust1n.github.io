<template>
	<div class="sect">
		<iframe allowtransparency="true" scrolling="no" frameborder="no" src="https://w.soundcloud.com/icon/?url=http%3A%2F%2Fsoundcloud.com%2Fch3njust1n&color=orange_white&size=32" style="width: 32px; height: 32px;"></iframe>

		<!-- <iframe src="https://open.spotify.com/embed/album/1DFixLWuPkv3KT3TnV35m3" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe> -->
	</div>
</template>

<script>

export default {
	name: 'music',
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