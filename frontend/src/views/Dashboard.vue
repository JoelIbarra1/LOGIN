<template>
    <div>
      <h2>Dashboard protegido</h2>
  
      <form @submit.prevent="createItem">
        <input v-model="newItem.title" placeholder="Título" />
        <input v-model="newItem.description" placeholder="Descripción" />
        <button type="submit">Crear Item</button>
      </form>
  
      <ul>
        <li v-for="item in items" :key="item.id">
          <div v-if="editItem.id !== item.id">
            <strong>{{ item.title }}</strong>: {{ item.description }}
            <button @click="startEdit(item)">Editar</button>
            <button @click="deleteItem(item.id)">Eliminar</button>
          </div>
  
          <div v-else>
            <input v-model="editItem.title" placeholder="Título" />
            <input v-model="editItem.description" placeholder="Descripción" />
            <button @click="updateItem(item.id)">Guardar</button>
            <button @click="cancelEdit">Cancelar</button>
          </div>
        </li>
      </ul>
  
      <button @click="logout">Cerrar sesión</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        items: [],
        newItem: {
          title: '',
          description: ''
        },
        editItem: {
          id: null,
          title: '',
          description: ''
        }
      }
    },
    mounted() {
      this.fetchItems()
    },
    methods: {
      async fetchItems() {
        const token = localStorage.getItem('token')
        const res = await fetch('http://localhost:8000/items/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        this.items = await res.json()
      },
      async createItem() {
        const token = localStorage.getItem('token')
        await fetch('http://localhost:8000/items/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`
          },
          body: JSON.stringify(this.newItem)
        })
        this.newItem.title = ''
        this.newItem.description = ''
        this.fetchItems()
      },
      async deleteItem(id) {
        const token = localStorage.getItem('token')
        await fetch(`http://localhost:8000/items/${id}`, {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        this.fetchItems()
      },
      startEdit(item) {
        this.editItem = { ...item }
      },
      cancelEdit() {
        this.editItem = { id: null, title: '', description: '' }
      },
      async updateItem(id) {
        const token = localStorage.getItem('token')
        await fetch(`http://localhost:8000/items/${id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`
          },
          body: JSON.stringify({
            title: this.editItem.title,
            description: this.editItem.description
          })
        })
        this.cancelEdit()
        this.fetchItems()
      },
      logout() {
        localStorage.removeItem('token')
        this.$router.push('/login')
      }
    }
  }
  </script>
  
  <style scoped>
.dashboard-container {
  min-height: 100vh;
  background-color: #1e1e2f;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.dashboard-box {
  background-color: #2a2a40;
  padding: 30px 40px;
  border-radius: 12px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  color: white;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 25px;
}

input {
  padding: 10px;
  border: none;
  border-radius: 8px;
  background-color: #3b3b55;
  color: white;
}

input::placeholder {
  color: #ccc;
}

button {
  padding: 10px;
  border: none;
  border-radius: 8px;
  background-color: #4c70ff;
  color: white;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s ease;
}

button:hover {
  background-color: #3d5be8;
}

.item-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.item {
  background-color: #3a3a55;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 12px;
}

.item-view, .item-edit {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.actions {
  display: flex;
  gap: 10px;
}

.actions button {
  flex: 1;
}

.delete {
  background-color: #e03c3c;
}

.delete:hover {
  background-color: #c02d2d;
}

.cancel {
  background-color: #777;
}

.logout {
  width: 100%;
  margin-top: 20px;
  background-color: #555;
}

.logout:hover {
  background-color: #444;
}
</style>