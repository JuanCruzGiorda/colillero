<template>
    <div id="app">
      <headerComponent/>
      <div class="contenido">
        <section class="colillero">
          <h1>Colilleros de la Facultad </h1>
          <a href="#" class="logo-link"></a>
          <div class="menu-grid">
            <colilleroItem v-for="colillero in colilleros" :key="colillero.id" :colillero="colillero"></ColilleroItem>
          </div>
        </section>
      </div>
    </div>
</template>
    
<script>
/* eslint-disable */
import headerComponent from './headerComponent.vue';
import axios from 'axios';
import colilleroItem from './colilleroItem.vue';
    
    export default {
      data() {
        return {
          colilleros: []
        };
      },
      components: {
        headerComponent,
        colilleroItem
  },
      mounted() {
        this.cargarColilleros();
      },
      methods: {
        cargarColilleros() {
          axios.get('http://127.0.0.1:8000/api/colillero/')
            .then(response => {
              this.colilleros = response.data;
            })
            .catch(error => {
              console.error('Error fetching colillero', error);
            });
        }
      }
    }
    </script>
  
<style>
body {
  background-color: white;
  font-family: 'Roboto', sans-serif;
  margin: 0;
  padding: 0px;
}

.contenido{
    background-color: white;
}

.colillero{
    padding: 2rem;
    text-align: center;
}

h1 {
    margin-top: -20px;
    font-size: 50px;
    text-align: center;
    padding: 50px;
    color: #000000;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    justify-content: center;
}
</style>