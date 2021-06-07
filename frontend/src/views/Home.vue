<template>
  <div>
    <div v-for="(usuario, index) in users" :key="usuario.nombre + index">
      <span
        >nombre : {{ usuario.nombre }} ocupacion: {{ usuario.ocupacion }}</span
      >
    </div>
    <button @click="clickButton">evento</button>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      users: []
    }
  },
  mounted() {
    this.$axios.get("users").then((r) => {
      this.users = r.data
    })
  },
  sockets: {
    connect: function (data) {
      console.log(data)
    },
    myEvent: function (data) {
      this.users.push(data)
    }
  },
  methods: {
    clickButton: function () {
      this.$socket.emit("my event")
    }
  }
}
</script>
