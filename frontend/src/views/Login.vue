<template>
    <div>
      <h2>Login</h2>
      <input v-model="username" placeholder="Usuario" />
      <input v-model="password" placeholder="Contraseña" type="password" />
      <button @click="login">Iniciar sesión</button>
  
      <p>
        ¿No tienes cuenta?
        <router-link to="/register">Regístrate aquí</router-link>
      </p>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
        async login() {
            try {
                const formData = new URLSearchParams()
                formData.append('username', this.username)
                formData.append('password', this.password)

                const res = await axios.post('http://localhost:8000/token', formData, {
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
                })

                localStorage.setItem('token', res.data.access_token)
                this.$router.push('/dashboard')
            } catch (err) {
                alert('Credenciales incorrectas')
            }
        }
    }
  }
  </script>
  
  
<style scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #1e1e2f;
  padding: 20px;
}

.form-box {
  background-color: #2a2a40;
  padding: 30px 40px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 400px;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

h2 {
  text-align: center;
  font-weight: 600;
  margin-bottom: 10px;
}

input {
  padding: 12px;
  border: none;
  border-radius: 8px;
  outline: none;
  font-size: 14px;
  background-color: #3b3b55;
  color: white;
}

input::placeholder {
  color: #cccccc;
}

button {
  padding: 12px;
  background-color: #4c70ff;
  border: none;
  border-radius: 8px;
  color: white;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #3d5be8;
}

.register-link {
  text-align: center;
  font-size: 14px;
}

.register-link a {
  color: #4c70ff;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>