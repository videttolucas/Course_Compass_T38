<!--Created by: John Montesa-->
<!-- This is the Signup page for Course Compass -->
<!-- Users will be prompted with an email and password input. -->
<!-- They can also be redirected to the login page if they already have an account -->
<!-- They must also confirm their email and password to make sure they are correct -->
<!-- They are also able to choose a major from a major list -->

<template>
    <div class="signup-container">
        <div class="left-section">
            <br>
            <h2>Sign Up</h2>

            <form @submit.prevent="handleSubmit">
                <div class="name-container">
                    <input v-model="firstname" type="text" placeholder="First Name" required>
                    <input v-model="lastname" type="text" placeholder="Last Name" required>
                </div>
                <br>

                <input v-model="email" type="email" placeholder="Email" required>
                <br>
                <input v-model="confirmEmail" type="email" placeholder="Confirm Email" required>
                <br>
                <br>

                <div class="password-container">
                    <input v-model="password" ref="passwordInput" type="password" id="passwordInput" placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}" title="Passwords contain at least one lowercase and one uppercase letter, one number, one special character, and are at least 8 or more characters." required/>
                    <img class="eye-icon" :src="eyeIcon('passwordInput')" alt="Password Visibility Eye" @click="toggleVisibility('passwordInput')" />
                </div>
                <div class="password-container">
                    <input v-model="confirmPass" ref="confirmPasswordInput" type="password" id="confirmPasswordInput" placeholder="Confirm Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}" title="Passwords contain at least one lowercase and one uppercase letter, one number, one special character, and are at least 8 or more characters." required/>
                    <img class="eye-icon" :src="eyeIcon('confirmPasswordInput')" alt="Confirm Password Visibility Eye" @click="toggleVisibility('confirmPasswordInput')" />
                </div>
                <br>

                <div>
                    <label for="major">Select Your Major:</label>
                    <select v-model="selectedMajor" id="major" required>
                        <option value="" disabled></option>
                        <option v-for="major in majors" :key="major" :value="major">{{ major }}</option>
                    </select>
                </div>
                <br>


                <div class="button-container">
                    <button type="submit">Sign Up</button>
                </div>
            </form>


            <div class="signup-link">
                <p>Already have an account? <router-link to="/login">Log In</router-link></p>
            </div>
        </div>
    

        <div class="right-section">
            <img src="@/assets/background-img.png" alt="Background Image" />
        </div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
            firstname: '',
            lastname: '',
            email: '',
            confirmEmail: '',
            password: '',
            confirmPass: '',
            passwordVis: false,
            confirmPassVis: false,
            selectedMajor: '',

            majors:[
                'Accounting',
                'Agricultural Science',
                'Anthropology',
                'Art',
                'Biochemistry',
                'Biology',
                'Business Administration',
                'Chemistry',
                'Civil Engineering',
                'Computer Science',
                'Criminal Justice',
                'Economics',
                'Electrical Engineering',
                'English',
                'Environmental Science',
                'Finance',
                'Geography',
                'History',
                'Journalism',
                'Management',
                'Marketing',
                'Mathematics',
                'Mechanical Engineering',
                'Music',
                'Nursing',
                'Nutrition',
                'Philosophy',
                'Physics',
                'Political Science',
                'Psychology',
                'Social Work',
                'Sociology',
                'Spanish',
                'Statistics',
                'Theatre',
                'Wildlife Ecology and Conservation'],
            };
        },

    methods: {
        toggleVisibility(refName) {
            const inputField = this.$refs[refName];
            if (inputField) {
                if (refName === 'passwordInput') {
                this.passwordVis = !this.passwordVis;
                inputField.type = this.passwordVis ? 'text' : 'password';
                } else if (refName === 'confirmPasswordInput') {
                this.confirmPassVis = !this.confirmPassVis;
                inputField.type = this.confirmPassVis ? 'text' : 'password';
                }
            }
        },

        eyeIcon(refName) {
            return refName === 'passwordInput'
                ? this.passwordVis
                ? require('../assets/eyeclose.png')
                : require('../assets/eye.png')
                : this.confirmPassVis
                ? require('../assets/eyeclose.png')
                : require('../assets/eye.png');
        },

        validateForm() {
            if (this.email !== this.confirmEmail || this.password !== this.confirmPass) {
                alert('Emails and Passwords must match.');
                return false;
            }
            return true;
        },

        async handleSubmit() {
        if (this.validateForm()) {
            try {
                const response = await this.axios.post('http://localhost:5000/signup', {
                    Fname: this.firstname,
                    Lname: this.lastname,
                    Email: this.email,
                    Passwd: this.password,
                    majorID: this.getMajorsID(this.selectedMajor)  // Assuming you have a method to convert major name to ID
                });
                alert('Registration successful!');
                this.$router.push('/login'); // Redirect to login page after signup
            } catch (error) {
                alert('Registration failed: ' + error.response.data.message);
            }
        }
        },
    },
};
</script>

<style scoped>
    .name-container {
        display: flex;
        gap: 10px;
    }
    .signup-container {
        display: flex;
        height: 100vh;
    }

    .left-section {
        flex: 1;
        padding: 20px;
        border-right: 1px solid #000000;
    }

    .right-section {
        flex: 1;
        overflow: hidden;
    }

    img {
        height: 100%;
        width: auto;
        object-fit: cover;
    }

    :placeholder-shown{
        font-family: Poppins, sans-serif;
    }

    option {
        font-family: Poppins, sans-serif;
    }
    h2 {
        text-align: left;
        font-family:akira;
    }

    p{
        font-family: Poppins, sans-serif;
    }

    .logo {
        max-width: 100px;
        margin-bottom: 20px;
    }

    input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
    }

    label{
        font-family: Poppins, sans-serif;
        font-size: 18px;
    }

    .button-container {
        text-align: right;
    }

    button {
        font-family: akira, sans-serif;
        background-color: #000000;
        color: #ffffff;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s linear, color 0.3s linear;
    }

    button:hover {
        background-color: #555555;
    }

    .signup-link {
        margin-top: 20px;
    }

    .signup-link a {
        color: #1292e7;
        text-decoration: none;
    }

    .signup-link a:hover {
        text-decoration: underline;
    }

    .password-container {
        position: relative;
    }

    .eye-icon {
        position: absolute;
        margin-left: -45px;
        margin-top: 25px;
        width: 30px;
        height: auto;
        cursor: pointer;
    }

    select {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
    }

</style>