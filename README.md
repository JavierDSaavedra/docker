# Docker Compose - Proyecto FACE-UBB

Orquestación de contenedores para el proyecto institucional de la Facultad de Ciencias de la Universidad del Bío-Bío.

## Estructura del Proyecto

Este proyecto está compuesto por los siguientes servicios:

- **taller-desarrollo**: Frontend React + Vite (Taller de Desarrollo) - Puerto 5174
- **infraestructura**: Frontend estático (Estructura Institucional) - Puerto 3001
- **generador**: Backend de generación - Puerto 3000  
- **usuario**: Servicio de usuarios - Puerto 5173
- **plantillas**: Servicio de plantillas - Puerto 8080
- **nginx**: Proxy inverso - Puerto 80

## Requisitos Previos

- Docker (versión 20.10 o superior)
- Docker Compose (versión 2.0 o superior)

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/mi-proyecto.git
cd mi-proyecto
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

El archivo `.env.example` contiene todas las variables necesarias con valores por defecto. Modifica el `.env` si necesitas cambiar puertos o configuraciones específicas.

### 3. Levantar los servicios

```bash
docker compose up --build
```

Para ejecutar en segundo plano:

```bash
docker compose up -d --build
```

## Acceso a los Servicios

Una vez que todos los contenedores estén levantados, accede a los servicios:

| Servicio | URL | Puerto |
|----------|-----|--------|
| Frontend (Taller de Desarrollo - React) | http://localhost:5174 | 5174 |
| Infraestructura (Estructura Institucional) | http://localhost:3001 | 3001 |
| Generador (Backend) | http://localhost:3000 | 3000 |
| Usuario | http://localhost:5173 | 5173 |
| Plantillas | http://localhost:8080 | 8080 |
| Nginx Proxy | http://localhost | 80 |

## Comandos Útiles

### Ver logs de un servicio específico

```bash
docker compose logs frontend
docker compose logs generador
```

### Ver logs en tiempo real

```bash
docker compose logs -f
```

### Detener los servicios

```bash
docker compose stop
```

### Detener y eliminar contenedores

```bash
docker compose down
```

### Reconstruir imágenes

```bash
docker compose build --no-cache
```

### Reiniciar un servicio

```bash
docker compose restart frontend
```

## Estructura de Directorios

```
.
├── docker-compose.yml          # Configuración de Docker Compose
├── .env.example                # Plantilla de variables de entorno
├── README.md                   # Este archivo
├── frontend/                   # Frontend React + Vite
│   ├── Dockerfile
│   ├── package.json
│   └── src/
├── Generador/                  # Backend de generación
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── Usuario/                    # Servicio de usuarios
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── Plantillas/                 # Servicio de plantillas
│   └── Dockerfile
└── Estructura institucional/    # Nginx
    ├── Dockerfile
    ├── nginx.conf
    └── index.html
```

## Redes y Comunicación

El proyecto define dos redes Docker para aislar servicios:

- **frontend_network**: Conecta los servicios frontend
- **backend_network**: Conecta los servicios backend

## Health Checks

Los servicios cuentan con health checks automatizados:

- **frontend**: Verifica disponibilidad cada 30 segundos
- **generador**: Verifica el endpoint `/health` cada 30 segundos

## Notas de Desarrollo

- Los servicios están configurados con `restart: unless-stopped` para reiniciar automáticamente en caso de fallo.
- Los puertos pueden configurarse mediante variables de entorno en el archivo `.env`.
- Los logs se pueden consultar usando `docker compose logs`.

## Solución de Problemas

### "El contenedor ya existe"

Si recibes un error de conflicto de contenedor:

```bash
docker container prune -f
docker compose up -d --build
```

### "Puerto ya está en uso"

Cambia los puertos en el archivo `.env`:

```
FRONTEND_PORT=3002
GENERADOR_PORT=3001
```

Luego ejecuta:

```bash
docker compose up -d
```

### Ver proceso de construcción detallado

```bash
docker compose up --build --verbose
```

## Contribuciones

Para cambios significativos, por favor abre un issue primero para discutir qué te gustaría cambiar.

## Licencia

Este proyecto es parte del programa académico de la Universidad del Bío-Bío.
