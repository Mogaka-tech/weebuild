<template>
  <div class="home">
    <div
      class="drop-zone"
      @drop="onDrop($event, 1)"
      @dragenter.prevent
      @dragover.prevent
    >
      <div
        v-for="item in getList(1)"
        :key="item.id"
        class="drag-el"
        draggable="true"
        @dragstart="startDrag($event, item)"
      >
        {{ item.title }}
      </div>
    </div>
    <div
      class="drop-zone"
      @drop="onDrop($event, 2)"
      @dragenter.prevent
      @dragover.prevent
    >
      <div
        v-for="item in getList(2)"
        :key="item.id"
        class="drag-el"
        draggable="true"
        @dragstart="startDrag($event, item)"
      >
        {{ item.title }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "Home",
  setup() {
    const items = ref([
      { id: 0, title: "Item A", list: 1 },
      { id: 1, title: "Item B", list: 1 },
      { id: 2, title: "Item C", list: 2 },
    ]);

    const getList = (list) => {
      return items.value.filter((item) => item.list == list);
    };

    const startDrag = (event, item) => {
      console.log(item);
      event.dataTransfer.dropEffect = "move";
      event.dataTransfer.effectAllowed = "move";
      event.dataTransfer.setData("itemID", item.id);
    };

    const onDrop = (event, list) => {
      const itemID = event.dataTransfer.getData("itemID");
      const item = item.value.find((item) => item.id == itemID);
      item.list = list;
    };

    return {
      getList,
      onDrop,
      startDrag,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  grid-column-start: 2;
  grid-column-end: span 5;
}
.drop-zone {
  background-color: #eee;
  margin-bottom: 10px;
  padding: 10px;
  width: 50%;
  margin: 50px auto;
  min-height: 10px;
}

.drag-el {
  background-color: rgb(9, 205, 231);
  color: white;
  margin-bottom: 10px;
  padding: 5px;
}

.drag-el:nth-last-of-type(1) {
  margin-bottom: 0;
}
</style>
