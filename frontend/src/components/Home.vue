<!-- Created by: John Montesa-->
<!-- This is the home page for Course Compass, which includes the navigation bar, a description of the website, and a button to get started-->
<!-- This is the first page the user will see -->

<template>
    <br>
    <br>
    <h1>Remove the clutter of your college experience.</h1>
    <h1>Use Course Compass.</h1>
    <br>

    <img src="@/assets/unrskyline.png" alt="Unr whole campus with skyline">
    <br>
    <br>

    <div class="button-container">
        <router-link to="/signup">
            <button class="get-started-button">Get Started</button>
        </router-link>
    </div>
    <br>
    <br>
    <br>
    <br>
</template>

<script>
</script>

<style scoped>
    p{
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
    }

    h1{
        font-family: 'akira', akira;
        text-align: center;
        color:#000000;
    }

    img {
        width: 100%;
        height: auto;
    }

    .button-container {
        margin: 0;
        padding: 0;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .get-started-button {
        font-family: akira;
        background-color: #000000;
        color: #ffffff;
        padding: 10px 30px;
        font-size: 30px;
        border: none;
        cursor: pointer;
        display: inline-block;
        transition: background-color 0.3s linear, color 0.3s linear;
        text-decoration: none;
    }

    .get-started-button:hover {
        background-color: #ffffff;
        color: #000000;
    }
</style>