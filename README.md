#  Proyecto de Login con FastAPI y Vue.js

##  Descripción

Este proyecto consiste en un sistema completo de autenticación y autorización de usuarios, desarrollado con **FastAPI** para el backend y **Vue.js** para el frontend. El objetivo principal es proteger rutas específicas del frontend (como un panel de usuario) que solo deben ser accesibles si el usuario ha iniciado sesión correctamente.

El sistema de autenticación se basa en **JSON Web Tokens (JWT)**, una tecnología moderna, segura y ampliamente adoptada para gestionar sesiones sin necesidad de almacenar estados en el servidor.

Este proyecto es ideal para quienes desean una base sólida para aplicaciones web con frontend moderno y backend robusto.

---

##  Cómo comenzar

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Configura el entorno del backend

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configura el entorno del frontend

```bash
cd frontend
npm install
```

### 4. Ejecuta el backend

```bash
uvicorn app.main:app --reload
```

### 5. Ejecuta el frontend

```bash
cd frontend
npm run dev
```

---

##  Tecnologías utilizadas

### Backend (FastAPI)

- **FastAPI**: Framework web rápido basado en Python.
- **SQLAlchemy**: ORM para manejar la base de datos.
- **JWT (via jose)**: Para manejo de autenticación segura.
- **Pydantic**: Validación de datos.
- **SQLite**: Base de datos ligera para pruebas.

### Frontend (Vue.js)

- **Vue 3** con Composition API
- **Axios**: Cliente HTTP para comunicar con el backend.

---

##  Estructura del proyecto

```
 app/
 ┣ routers/
 ┃ ┣ items.py        # Rutas protegidas relacionadas con ítems (solo para usuarios autenticados)
 ┃ ┗ users.py        # Endpoints para gestión de usuarios (listar, obtener)
 ┣ auth.py           # Lógica de login, creación de tokens y verificación de credenciales
 ┣ crud.py           # Funciones de lectura/escritura a la base de datos (usuarios, ítems)
 ┣ database.py       # Configuración y conexión de la base de datos SQLite
 ┣ models.py         # Modelos ORM de SQLAlchemy (Usuario, Ítem, etc.)
 ┣ schemas.py        # Esquemas de validación con Pydantic
 ┗ main.py           # Punto de entrada de FastAPI (monta routers, middleware, CORS)

 frontend/
 ┣ src/
 ┃ ┣ views/
 ┃ ┃ ┣ Login.vue       # Componente de login con formulario y lógica de autenticación
 ┃ ┃ ┣ Register.vue    # Componente de registro de nuevos usuarios
 ┃ ┃ ┗ Dashboard.vue   # Vista protegida que solo se puede acceder con sesión activa
 ┃ ┣ router/
 ┃ ┃ ┗ index.js        # Configuración de rutas con protección mediante guardias de navegación
 ┃ ┗ App.vue           # Componente principal de Vue
 ┗ main.js             # Punto de entrada del frontend, monta la app Vue y sus rutas
```

---

##  Seguridad y protección de rutas

- El sistema usa **JWT** para manejar sesiones. Al iniciar sesión correctamente, el servidor retorna un token que se guarda en el cliente (localStorage).
- Las rutas protegidas en el backend requieren que el token sea enviado en el encabezado `Authorization`.
- En el frontend, se protege la ruta de `Dashboard.vue` usando guardias de navegación de Vue Router. Si no hay token, se redirige automáticamente al login.

---

##  Funcionalidades implementadas

- Registro de usuarios con validación básica.
- Login de usuarios con almacenamiento del token JWT.
- Redirección automática en frontend según el estado de autenticación.
- Acceso a información protegida desde el backend.
- Separación clara de responsabilidades entre backend y frontend.

---

¡Gracias por revisar este proyecto!
