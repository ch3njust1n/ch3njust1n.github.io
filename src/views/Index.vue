<template>
	<div id="main">
		<Contact></Contact>
		<About></About>
		<Music></Music>
		<News></News>
		<MIC></MIC>
		<Projects></Projects>
		<Edu></Edu>
	</div>
</template>

<script>
import About from '@/components/about'
import Music from '@/components/music'
import News from '@/components/news'
import MIC from '@/components/mic'
import Contact from '@/components/contact'
import Projects from '@/components/projects'
import Edu from '@/components/education'

export default {
	name: 'index',
	components: {
		About,
		Music,
		News,
		MIC,
		Contact,
		Projects,
		Edu
	},
	data () {
		return {
			name: 'justinchen'
		}
	},
	methods: {

	}
}
</script>

<style>
#main {
	margin: 1em 4em;
}

#home {
	display: inline;
}

.sect {
	margin: 2em 0;
}

.sect h1 {
	font-size: 1.2em;
	margin-bottom: .5em;
}

.sect p {
	font-size: 14px
}

.item {
	margin: 1em 0 1.5em 0;
	display: flex;
	flex-direction: column;
}

.item-header {
	font-weight: 600;
}

.item-name {
	margin-bottom: 5px;
	font-size: 14px;
}

.item-venu {
	font-size: 14px;
}

.item-auth {
	margin-top: 5px;
	font-size: 14px;
}

.item-desc {
	margin-top: .5em;
	font-size: 14px;
}

.item-year {
	font-size: 13px;
}

h1 {
	/*text-transform: uppercase;*/
	font-size: 1em;
}

@media screen and (max-width: 600px) {

}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {

}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {

}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {

}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {

}
</style>
