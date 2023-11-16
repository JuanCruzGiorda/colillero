<template>
  <div class="colillero-item" :class="getColilleroClass()">
    <h2>{{ colillero.ubicacion }}</h2>
  </div>
  </template>
  
  <script>
  /* eslint-disable */
  export default {
  props: {
    colillero: Object,
    required: true
  },
  methods: {
    getColilleroClass() {
      if (this.colillero.estado === 'vacio') {
        return 'verde';
      } else if (this.colillero.estado === 'porllenarse') {
        return 'amarillo';
      } else if (this.colillero.estado === 'lleno') {
        return 'rojo';
      }
    },
  },
};
</script>
    
<style>
.verde {
  background-color: rgb(10, 181, 10);
}

.amarillo {
  background-color: yellow;
}

.rojo {
  background-color: red;
}

.colillero-item {
  padding: 1rem;
  border: 1px solid #000;
  text-align: center;
  color: black;
  border-radius: 8px;
  transition: background-color 0.3s ease;
  transition: transform 0.5s ease;
}

.colillero-item:hover {
  cursor: pointer;
  transform: scale(1.05);
}
</style>
  