<!--Created by: John Montesa-->
<!-- This is the courses page for Course Compass -->
<!-- This page prompts the user...... -->

<template>
    <!--<img src="@/assets/unrquad.png" alt="Unr quad">-->
    <br>
    <h1>Courses</h1>

    <div class="container mt-3">
        <div class="row">
            <div class="col-md-3">
                    <FilterMenu></FilterMenu>
            </div>            
            <div class="col-md-auto ml-auto">

            </div>
        </div>
    </div>
</template>

<script>
    import FilterMenu from '@/components/FilterMenu.vue'

    export default{
        name: 'Courses',
        components:
        {
            FilterMenu
        }
    }
</script>

<style scoped>
    .container{
        margin: 30px;
        padding: 0px;
        overflow: hidden;
    }
    p{
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
    }
    h1{
        font-family: 'akira', akira;
        text-align: left;
        margin-left: 30px;
    }

    img {
        max-width: 100%;
        height: auto; /* Maintain the image's aspect ratio */
    }
</style>