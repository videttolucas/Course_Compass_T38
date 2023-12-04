<template>
    <div class="progress-page">
        <div v-for="(major, index) in filteredMajors" :key="index">
            <div>
            <h1>{{ major.name }}</h1>
            <div class="course-container" v-for="(course, courseIndex) in major.courses" :key="courseIndex">
                <input type="checkbox" v-model="course.completed" />
                <label>{{ course.name }}</label>
            </div>
            </div>
        </div>
    </div>

    <div class="footer">
        <div class="container-fluid mt-3">
            <div class="row">
                <div v-if="selectedMajor === user.major" class="col-sm-2 d-flex">
                    <div class="completion-text">Progress:</div>
                </div>

                <div class="col d-flex flex-column">
                    <div class="progress-container">
                        <div v-if="selectedMajor === user.major" class="progress-bar" :style="{ width: `${progressPercentage}%` }">
                            <span class="progress-text">{{ Math.round(progressPercentage) }}%</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                user: {
                    firstname: 'John',
                    lastname: 'Montesa',
                    email: '',
                    major: 'Computer Science & Engineering',
                },
                majors: [
                {
                    name: 'Computer Science & Engineering',
                    courses: [
                        { name: 'CS 135', completed: false },
                        { name: 'CS 202', completed: false },
                        { name: 'CS 219', completed: false },
                        { name: 'CS 302', completed: false },
                        { name: 'CS 365', completed: false },
                        { name: 'CS 425', completed: false },
                        { name: 'CS 426', completed: false },
                        { name: 'CS 446', completed: false },
                        { name: 'CS 456', completed: false },
                        { name: 'CS 477', completed: false },
                    ],
                },
                {
                    name: 'Electrical Engineering',
                        courses: [
                        { name: 'EE 101', completed: false },
                        { name: 'EE 202', completed: false },
                        { name: 'EE 303', completed: false },
                    ],
                },
                ],

                selectedMajor: null,
            };
        },
    
        created() {
            this.selectedMajor = this.user.major; 
        },

        computed: {
            filteredMajors() {
                return this.majors.filter((major) => major.name === this.user.major);
            },
            progressPercentage() {
                const selectedMajorCourses = this.majors.find((major) => major.name === this.user.major).courses;
                const completedCourses = selectedMajorCourses.filter((course) => course.completed).length;
                const totalCourses = selectedMajorCourses.length;
                return (completedCourses / totalCourses) * 100;
            },
        },
    };
</script>

<style scoped>
    h2 {
        font-family: 'akira', akira;
        text-align: left;
        margin-left: 30px;
    }

    h1{
        font-family: 'akira', akira;
        text-align: center;
        margin-left: 30px; 
    }

    .progress-page {
        width: 100%;
        margin: 10px auto;
    }

    input[type="checkbox"] {
        margin-right: 8px;
    }

    .progress-container {
        height: 25px;
        display: flex;
        border: 2px solid #000000;
        border-radius: 10px;
        margin-right: 15px;
    }

    .progress-bar {
        height: 100%;
        background: #54ff59;
        position: relative;
        transition: width 0.3s ease;
        border-radius: 10px;
    }

    .progress-text {
        position: absolute;
        font-family:akira;
        color: #000;
        margin-left: 10px;
    }

    .completion-text {
        font-family: akira;
        margin:  3px auto;
        color: #000;
        font-size: 18px;
    }

    .footer { 
        position: absolute;
        bottom: 0; 
        left: 0;
        padding: 10px;
        width: 100%;
    }

    .course-container {
        font-family: Popins, sans-serif;
        align-items: center;
        padding: 8px;
    }

</style>
