<template>
  <Login></Login>
</template>

<script>
import Login from '@/components/Login.vue'

export default {
  name: 'LoginView',
  components: {
    Login
  },
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await this.axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        });
        
        const { token, expires } = response.data;
        
        localStorage.setItem('userToken', token);
        localStorage.setItem('tokenExpiration', expires);

        this.$router.push('/home');  // Redirect to home
      } catch (error) {
        if (error.response && error.response.status === 401) {
          this.errorMessage = 'Incorrect email or password. Please try again.';
        } else {
          this.errorMessage = 'An error occurred. Please try again later.';
        }
      }
    }
  }
}
</script>