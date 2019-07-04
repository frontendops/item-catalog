<template>
  <div class="home">
    {{ msg }}
    <h2>I am from Vue</h2>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "home",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>
