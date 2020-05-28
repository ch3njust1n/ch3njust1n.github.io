<template>
    <div class="sect">
        <h1>education</h1>
        <div class="creds">
            <ul class="degrees">
                <li v-for="(i, id) in creds" :key="id">{{ i.school }}, {{ i.degree }}, {{ i.major }}</li>
            </ul>
        </div>

        <div class="coursework">
            <span class="sub-head">Graduate coursework</span>
            <ul>
                <li v-for="(i, id) in grad" :key="id">{{ i.name }}</li>
            </ul>
        </div>
        <div class="coursework">
            <span class="sub-head">Undergraduate coursework</span>
            <ul>
                <li v-for="(i, id) in ugrad" :key="id">{{ i.name }}</li>
            </ul>
        </div>
    </div>
</template>

<script>
import courses from '@/json/courses'
export default {
    name: 'education',
    components: {
    },
    data() {
        return {
            creds: [
                {"school": "Boston University", "degree": "M.S.", "major": "Computer Science"},
                {"school": "Boston University", "degree": "B.A.", "major": "Computer Science"}
            ],
            grad: courses['grad'],
            ugrad: courses['ugrad']
        }
    },
    methods: {

    }
}
</script>

<style scoped>
.coursework {
    margin-bottom: 1em;
    font-size: 14px;
}

.sub-head {
    margin-bottom: 1em;
    font-size: 14px;
    font-weight: 600;
}

ul {
    margin-top: 10px;
}

ul li {
    margin-bottom: 5px;
    font-size: 14px;
}

.degrees {
    margin-bottom: 1em;
}
</style>