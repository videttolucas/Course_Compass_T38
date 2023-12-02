<!-- Created by: John Montesa -->
<!-- This component creates the navigation bar that the user will interact with -->
<!-- There are ___ buttons, and one drop down menu that directs the user to go -->

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
                <router-link to="/" class="navbar-brand">
                    <img src="../assets/course compass logo.png" alt="Course Compass Logo">
                </router-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <!-- right-aligned menu items -->
                    <li class="nav-item">
                        <router-link to="/courses" class = "nav-link">Courses</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/schedule" class = "nav-link">Schedule</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Checklist</a>
                    </li>
                    <li class="nav-item">
                        <router-link to="/about" class = "nav-link">About</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Account
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Log In</a></li>
                            <li><a class="dropdown-item" href="#">Sign Up</a></li>
                            <li><a class="dropdown-item" href="#">Profile Settings</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>

</script>

<style scoped>
    .navbar {
        background-color: #ffffff; /* Set background color to white */
        border-bottom: 2px solid #000000; /* Add a black border at the bottom */
    }

    .navbar-brand img {
        max-width: 95px;
        height: auto;
    }

    .nav-link {
        font-family: 'akira';            
        font-size: 27px;
        color: #160e0e; /* Set text color to black */
        margin-right: 10px;
    }

    .nav-link:hover {
        color: #ffffff; /* Set text color to white on hover */
        background-color: #000000; /* Set background color to black on hover */
    }

    .dropdown-menu {
        font-family: 'akira';
        background-color: #ffffff;
        border: 1px solid transparent;
        text-align: center;
    }

    .dropdown-item {
        color: #000000;
        border: 1px solid #000000;
        text-align: center;
    }

    .dropdown-item:hover {
        color: #ffffff;
        background-color: #000000;
    }
</style>
