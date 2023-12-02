<template>
  <div class="progress-page">
    <h2>Progress</h2>

    <!-- Your major array with checkboxes -->
    <div v-for="(course, index) in major" :key="index">
      <input type="checkbox" v-model="course.completed" @change="updateProgress" />
      <label>{{ course.name }}</label>
    </div>

    <!-- Progress bar -->
    <div class="progress-container">
      <div class="completion-text">Completion: {{ Math.round(progressPercentage) }}%</div>
      <div class="progress-bar" :style="{ width: `${progressPercentage}%` }">
        <span class="progress-text">{{ Math.round(progressPercentage) }}%</span>
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

/* Style your checkboxes and labels as needed */
input[type="checkbox"] {
  margin-right: 8px;
}

/* Style your progress bar */
.progress-container {
    height: 30px;
    display: flex;
    align-items: center;
    border: 1px solid #000000;
}

.progress-bar {
  height: 100%;
  background: repeating-linear-gradient(-45deg, #3bff42, #3bff42 10px);
  position: relative;
  transition: width 0.3s ease; /* Add transition for width changes */
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #000; /* Black text */
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
