<!--Created by: John Montesa-->
<!-- This is the Login page for Course Compass -->
<!-- Users will be prompted with an email and password input. The password input allows users to see what they were typing -->
<!-- They can also be redirected to the signup page if they do not have an account yet-->
<!-- There are specific parameters each form must meet to be able to log in -->

<template>
    <div class="login-container">
            <img class ="logo" src="../assets/course compass logo.png" alt="Course Compass Logo">
            <h2>Log In</h2>

            <!-- Input fields for email and password -->
            <form>
                <input type="email" placeholder="Email" required>
                <br>

                <div class="password-container">
                    <input ref="passwordInput" type="password" id="passwordInput" placeholder="Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}" title="Passwords contain at least one lowercase and one uppercase letter, one number, one special character, and are atleast 8 or more characters." required>
                    <img class ="eye-icon" :src="eyeIcon()" alt="Password Visibility Eye" @click="toggleVisibility">
                </div>
                <br>

                <div class="button-container">
                    <button type="submit">Log In</button>
                </div>

            </form>
            <div class="signup-link">
                <p>Don't have an account? <router-link to="/signup" >Sign Up</router-link></p>
            </div>
            <div class="signup-link">
                <p><router-link to="/signup" >Forgot Password?</router-link></p>
            </div>
        </div>
</template>

<script>
    export default{
        data(){
            return{
                email: '',
                password: '',
                passwordVis: false
            };
        },
        methods:{
            toggleVisibility(){
                const passwordInput = this.$refs.passwordInput;
                if (passwordInput) {
                    this.passwordVis = !this.passwordVis;
                    passwordInput.type = this.passwordVis ? 'text' : 'password';
                }
            },
            eyeIcon(){
                return this.passwordVis ? require('../assets/eyeclose.png') : require('../assets/eye.png');
            }
        }
    };
</script>

<style scoped>
    :placeholder-shown{
        font-family: Poppins, sans-serif;
    }

    h2 {
        margin-left: 30px;
        text-align: left;
        font-family:akira;
    }

    p{
        font-family: Poppins, sans-serif;
    }

    .login-container {
        background-color: #e1e1e1;
        margin: 5% auto;
        padding: 20px;
        max-width: 600px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        align-content: center;
        text-align: center;
    }

    .logo {
        max-width: 100px;
        margin-bottom: 20px;
    }

    input {
        width: 90%;
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
    }

    .button-container {
        margin-right: 30px;
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
</style>