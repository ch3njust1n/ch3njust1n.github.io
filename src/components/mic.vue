<template>
	<div class="sect">
		<h1>president, director and co-founder</h1>
		<ul>
			<li class="item" v-for="(i, id) in prog" :key="id">
				<span class="item-header">
					<a class="item-name" :href="i.link" v-if="i.link != null" target="_blank">
						{{ i.name }}
					</a>
					<span class="item-name" v-else>
						{{ i.name }}
					</span>
					<span class="item-year" v-if="i.year != null">, {{ i.year }}</span>
				</span>
				<p class="item-desc">{{ i.desc }}</p>
			</li>
		</ul>
	</div>
</template>

<script>

export default {
	name: 'index',
	components: {
	},
	data() {
		return {
			prog: [
				{"name": "Machine Intelligence Community, Inc.", "year": "2018-Present", "link":"https://machineintelligence.cc", "desc": "501(c)(3) nonprofit for making education on machine intelligence accessible, effective, and innovative."},
				{"name": "Machine Intelligence Conference", "desc": "MIC is a platform for student to share their work, breaking down institutional barriers, championing diversity and connecting students to industry professionals.", "year": "2018, 2019"},
				{"name": "student communities", "desc": "MIC, Inc. helped start and grow several student communities at Massachusetts Institute of Technology, Boston University, Harvard College, and SRM Amaravati and Kattankulathur.", "year": "2017-2020"}
			]
		}
	},
	methods: {

	}
}
</script>

<style scoped>
.item {
	margin-bottom: 1em;
}

.item-name {
	display: inline;
}

.item-desc {
	margin-top: 5px;
}
</style>