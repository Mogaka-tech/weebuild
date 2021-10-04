<template>
  <div class="parent">
    <div class="nav-bar"><h1>Navbar</h1></div>
    <div class="side-bar"><h1>Sidebar</h1><span>Components for the different sections</span></div>
    <div class="body">
      <h1>Body Content</h1>
      <span>Has the drag n' drop interface</span>
    </div>
    <div class="styling"><h2>Styling</h2></div>
    <div class="footer"><h1>Footer</h1></div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
};
</script>

<style scoped>
.parent {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: 60px repeat(3, 1fr) 60px;
  grid-column-gap: 5px;
  grid-row-gap: 5px;
  min-height: 100vh;
  min-width: 80vw;
  width: auto;
}

.nav-bar {
  border: 1px solid black;
  grid-column-start: 2;
  grid-column-end: 6;
  grid-row-start: 1;
}

.side-bar {
  grid-row-start: 1;
  grid-row-end: 6;
  border: 1px solid black;
}

.body {
  grid-column-start: 2;
  grid-column-end: 5;
  border: 1px solid black;
  grid-row-start: 2;
  grid-row-end: 5;
}

.styling {
  border: 1px solid black;
}

.footer {
  grid-column-start: 2;
  grid-column-end: 6;
  border: 1px solid black;
}
</style>
