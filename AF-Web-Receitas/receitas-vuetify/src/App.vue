<script setup>
</script>

<template>
  <v-app id="app">
    <router-view/>
  </v-app>
</template>

<style scoped>
#app{
  font-family: 'MyFont';
  position: relative;
}

#app::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://33622.cdn.simplo7.net/static/33622/sku/tecidos-tricoline-tecido-tricoline-branco-folhas-branco-ref-1316--p-1643918210736.png');
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 0.2; /* Ajuste a opacidade aqui */
}
</style>
