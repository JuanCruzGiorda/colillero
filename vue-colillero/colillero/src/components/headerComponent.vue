<template>
    <header class="header">
      <nav class="nav">
        <router-link to="/" class="logo-link">
          <img class="imagen" src="@/assets/cenicero.png" alt="Logo">
        </router-link>
        <router-link to="/" class="nav-link">Inicio</router-link>
        <router-link to="/menu" class="nav-link">Colilleros</router-link>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'headerComponent',
  }
  </script>
  
  <style>
  .header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 25px 5%; /* Ajuste del padding a 5% para mover más a la izquierda */
    background-color: #428bca;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .nav {
    display: flex;
    align-items: center;
  }
  
  .logo-link {
    text-decoration: none;
  }
  
  .imagen {
    width: 50px;
    height: auto;
    object-fit: contain;
    margin-right: 10px;
  }
  
  .nav-link {
    font-size: 16px;
    color: #050504;
    text-decoration: none;
    font-weight: 500;
    margin-right: 30px;
    margin-left: 20px; /* Ajuste del margen izquierdo para la palabra "Inicio" */
    position: relative;
  }
  
  .nav-link::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -6px;
    width: 100%;
    height: 2px;
    background: #050504;
    border-radius: 5px;
    transform: translateY(10px);
    opacity: 0;
    transition: .5s;
  }
  
  .nav-link:hover::after {
    transform: translateY(0);
    opacity: 1;
  }
  
  .active {
    font-weight: bold;
  }
  </style>
  