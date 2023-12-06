<!-- Created by: John Montesa -->
<!-- This is the Progress page for Course Compass -->
<!-- This page will show the progress of the specific user's college career in a progress bar style -->
<!-- The progress bar will be based on the courses that the user has completed -->
<!-- The user can check off the courses that they have completed and the progress bar and units completed will update accordingly -->

<template>
  <!-- <div class="progress-page">
    <h2>Progress</h2> -->

    <!-- Your major array with checkboxes -->
    <div v-for="(course, index) in major" :key="index">
      <input type="checkbox" v-model="course.completed" @change="updateProgress" />
      <label>{{ course.name }}</label>
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
      major: [
        { name: 'Course 1', completed: false },
        { name: 'Course 2', completed: false },
        { name: 'Course 3', completed: false },
        { name: 'Course 4', completed: false },
        { name: 'Course 5', completed: false },
        { name: 'Course 6', completed: false },
      ],
      totalCourses: 6, // Total number of courses for full progress
    };
  },
  computed: {
    // Calculate the progress percentage based on completed courses
    progressPercentage() {
      const completedCourses = this.major.filter((course) => course.completed).length;
      return (completedCourses / this.totalCourses) * 100;
    },
  },
  methods: {
    // Update progress when a checkbox is changed
    updateProgress() {
      // Implement any additional logic if needed
    },
  },
};
</script>

<style scoped>
.progress-page {
  max-width: 100%;
  margin: 10px;
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
  position: absolute;
  top: 50%;
  left: 0;
  transform: translate(0, -50%);
  padding-left: 5px;
  color: #000; /* Black text */
}
</style>
