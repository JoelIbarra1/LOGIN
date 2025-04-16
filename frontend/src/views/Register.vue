<template>
    <div>
      <h2>Registro</h2>
      <input v-model="name" placeholder="Nombre" />
      <input v-model="email" placeholder="Correo electrónico" />
      <input v-model="password" type="password" placeholder="Contraseña" />
      <button @click="register">Registrarse</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: ''
      }
    },
    methods: {
      async register() {
        try {
          await axios.post('http://localhost:8000/register', {
            name: this.name,
            email: this.email,
            password: this.password
          })
          alert('Registrado correctamente')
          this.$router.push('/login')
        } catch (err) {
          alert('Error en el registro')
          console.error(err)
        }
      }
    }
  }
  </script>
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
  
  html, body {
    height: 100%;
    margin: 0;
    font-family: 'Inter', sans-serif;
    background-color: #0e0e1a;
  }
  
  .register-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: #0e0e1a;
  }
  
  .form-box {
    background-color: #1e1e2f;
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    width: 100%;
    max-width: 400px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    color: #fff;
  }
  
  h2 {
    text-align: center;
    margin: 0;
    font-weight: 600;
    font-size: 24px;
  }
  
  input {
    padding: 12px;
    font-size: 15px;
    border: none;
    border-radius: 8px;
    background-color: #2f2f47;
    color: white;
    outline: none;
  }
  
  input::placeholder {
    color: #aaa;
  }
  
  button {
    padding: 12px;
    font-weight: 600;
    background-color: #4c70ff;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  button:hover {
    background-color: #365ce2;
  }
  </style>