<!-- Created by: John Montesa -->
<!-- This component creates the courses list that the user will interact with -->
<!-- Classes are displayed in a list matter, where the background color alternates from each course to provide better readability -->
<!-- Each item is shown as their course department, course number, and name of course -->


<template>
    <!-- Display the courses in a list -->
    <div class="course-list">
        <div v-for="(course, index) in courses" :key="index" class="course-item" @click="handleCourseClick(course)">
        {{ course.name }}
        </div>
        <CourseDetailsPopup v-if="selectedCourse" :course="selectedCourse" @close="closePopup" />
    </div>
</template>

<script>
    import CourseDetailsPopup from '@/components/CourseDetailsPopup.vue';

    export default {
        //the courses are passed in as a prop array
        props: {
            courses: Array,
        },
        data() {
            return {
                selectedCourse: null,
            };
        },
        methods: {
            handleCourseClick(course) {
                this.selectedCourse = course;
            },
            closePopup() {
                this.selectedCourse = null;
            },
        },
        components: {
            CourseDetailsPopup,
            },
        };
</script>

<style scoped>
    .course-list {
        width: 100%;
        flex-direction: column;
    }

    .course-item {
        font-family: akira;
        padding: 8px;
        box-sizing: border-box;
        margin-bottom: 1px;
        border-radius: 0px;
        border: 1px solid #000000;
        color: #000000;
        cursor: pointer;
    }
    .course-item:nth-child(even) {
        background: #dddddd;
    }

    .course-item:nth-child(odd) {
        background: #aaaaaa; 
    }
</style>
