<!-- CourseDetailsPopup.vue -->
<template>
    <div class="popup" @click="closepopup">
        <!--Pop up Screen with details of course-->
        <div class="popup-content" @click.stop>
            <button class="close-btn" @click="closepopup">
                <img src="../assets/X.png" alt="Close Button">
            </button>
            <h2>Course Details</h2>
            <div class="container">
                <div class="row">
                    <!--Left Side of Popup Page, Reveals Course Details-->
                    <div class="col-lg left-column">
                        <p><strong>Department:</strong> {{ course.department }}</p>
                        <p><strong>Name:</strong> {{ course.name }}</p>
                        <!-- For every instance that involves indexing an item, use v-for, however for now, this will cause errors for ones without -->
                        <p><strong>Professor:</strong> {{ course.professor[0] }}, {{ course.professor[1] }}</p>
                        <p><strong>Format:</strong> {{ course.format }}</p>
                        <br>
                        <p><strong>Term:</strong> {{ course.term }} | {{ course.program }}</p>
                        <p><strong>Units:</strong> {{ course.units }}</p>
                        <br>
                        <p><strong>Meeting Details:</strong></p>
                        <p><strong>Location:</strong> {{ course.location }}</p>
                        <p><strong>Days:</strong> {{ course.days[0] }} | {{ course.days[1] }}</p>
                        <p><strong>Meeting Time:</strong> {{ course.meetingtime }}</p>
                    </div>
                    
                    <!--Right Side of Popup Page, Shows User Thoughts-->
                    <div class="col-lg">
                        <p><strong>What Students Think:</strong></p>
                        <p>{{ course.keywords[0] }}, {{ course.keywords[1] }}, {{ course.keywords[2] }}, {{ course.keywords[3] }}</p>
                        <p><strong>Student Rating:</strong> {{ course.rating }}/5</p>
                        <hr>
                        <p><strong>What Students Say:</strong></p>
                    </div>
                    <div class="w-100"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            course: Object,
        },
        methods: {
            closepopup() {
                this.$emit('close');
                },
            },
        };
    </script>

<style scoped>
    .popup {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .popup-content {
        background: #ffffff;
        padding: 20px;
        border-radius: 8px;
        max-width: 1000px;
        width: 100%;
    }

    .left-column {
        border-right: 1px solid #000000; /* Black line between columns */
    }

    .close-btn {
        border: transparent;
        background: transparent;
        cursor: pointer;
        width: 60px;
        height: 60px;
    }

    img {
        width: 100%;
        height: auto;
    }

    h2{
        font-family: 'akira', akira;
        text-align: center;
        color:#000000;
    }
    p{
        font-family: Poppins, sans-serif;
    }
</style>
