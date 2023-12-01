<!-- Created by: John Montesa -->
<!-- This component creates the filter menu that the user will interact with -->
<!-- There are ___ buttons, which drop down to reveal different filters the user can use to filter classes-->
<!-- There are ___ buttons, which drop down to reveal different filters the user can use to filter classes-->
<!-- There are ___ buttons, which drop down to reveal different filters the user can use to filter classes-->

<template>
  <div class="sidebar-menu">
    <ul class="list-group">
      <li class="list-group-item" v-for="(menuItem, index) in menuItems" :key="index">
        <div v-if="menuItem.children && menuItem.children.length > 0" class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            {{ menuItem.label }}
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" v-for="(childItem, childIndex) in menuItem.children" :key="childIndex" @click="handleItemClick(childItem)">{{ childItem.label }}</a>
          </div>
        </div>
        <div v-else @click="handleItemClick(menuItem)">{{ menuItem.label }}</div>
      </li>
    </ul>
  </div>
</template>

<script>
    export default {
    data() {
        return {
        menuItems: [
            { label: 'Department',children: [{ label: 'Subitem 1.1' }, { label: 'Subitem 1.2' }] },
            { label: 'Level', children: [{ label: '0+' }, { label: '100+' }, { label: '200+' },
                                         { label: '300+' }, { label: '400+' }, { label: '500+' }, { label: '600+' },
                                         { label: '700+' }] },
            { label: 'Start Time', children: [{ label: '8-9 AM' }, { label: '10-11 AM' }, { label: '12-1 PM' },
                                             { label: '1-2 PM' }, { label: '3-4 PM' }, { label: '5-6 PM' }, { label: '7-8 PM' }]},
            { label: 'Professor', children: [{ label: 'Fill here with professor names' }, { label: 'Subitem 3.2' }] },
            { label: 'Rating', children: [{ label: 'Subitem 3.1' }, { label: 'Subitem 3.2' }] },
            { label: 'Item 3', children: [{ label: 'Subitem 3.1' }, { label: 'Subitem 3.2' }] },
            { label: 'Item 3', children: [{ label: 'Subitem 3.1' }, { label: 'Subitem 3.2' }] },
            { label: 'Item 3', children: [{ label: 'Subitem 3.1' }, { label: 'Subitem 3.2' }] },
            { label: 'Item 3', children: [{ label: 'Subitem 3.1' }, { label: 'Subitem 3.2' }] },
            ],
        };
    },
    methods: {
        handleItemClick(item) {
        this.$emit('itemSelected', item);
        },
    },
    };
</script>

<style scoped>
    .sidebar-menu{
        width: 100%;
        background-color: #ffffff; /* Adjust the background color as needed */
        overflow-y: auto;
        height: 100vh;

    }
    .list-group-item{
        font-family: 'akira', akira;
        text-align: left;
        border: 1px solid #000000;
        box-sizing: border-box;
        border-radius: 0px;
    }
    .btn-secondary.dropdown-toggle {
        font-family: 'akira';
        background-color: #ffffff;
        color: #000000;
        border: 1px solid transparent;
        text-align: center;
    }

    .btn-secondary.dropdown-toggle:hover {
        color: #ffffff;
        background-color: #000000;
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
