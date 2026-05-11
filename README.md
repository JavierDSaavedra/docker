
```bash
docker build -t generador ./Generador
docker build -t usuario ./Usuario
docker build -t plantillas ./Plantillas
docker build -t infraestructura "./Estructura institucional"

# Ejecutar contenedores (mapear puertos a localhost)
docker run -d --name generador -p 3000:3000 generador
docker run -d --name usuario -p 5173:5173 usuario
docker run -d --name plantillas -p 8080:8080 plantillas
docker run -d --name infraestructura -p 80:80 infraestructura
```

## 📍 Servicios

| Servicio | Puerto |
|----------|--------|
| Generador | 3000 |
| Usuario | 5173 |
| Plantillas | 8080 |
| Infraestructura | 80 |

## 🛑 Detener

```bash
# Parar contenedores
docker stop generador usuario plantillas infraestructura

# Eliminar contenedores
docker rm generador usuario plantillas infraestructura

# (Opcional) Eliminar imágenes
docker rmi generador usuario plantillas infraestructura
```

## 📊 Comandos

```bash
# Ver estado
docker ps

# Ver logs (ejemplo)
docker logs -f generador

# Entrar en contenedor
docker exec -it generador sh
```

## 🔗 Comunicación entre Servicios

```javascript
// Desde Usuario → Generador
fetch('http://generador:3000/api')

// Desde Generador → Plantillas
fetch('http://plantillas:8080/templates')

// Desde Usuario → Infraestructura
fetch('http://infraestructura:80/static')
```

## 📁 Estructura

```
docker/
├── Generador/               (Node 3000)
│   └── Dockerfile
├── Usuario/                 (Node 5173)
│   └── Dockerfile
├── Plantillas/              (Node 8080)
│   └── Dockerfile
├── Estructura institucional/ (Nginx 80)
│   └── Dockerfile
├── README.md
├── QUICKSTART.md
├── .env.example
└── .gitignore
```
# docker

## 🧩 Despliegue con Docker Compose

Se agregó un archivo `docker-compose.yml` en la raíz para orquestar los servicios
existentes (`Generador`, `Usuario`, `Plantillas`, `Estructura institucional`).

Pasos rápidos:

1. Copiar la plantilla de variables de entorno:

```bash
cp .env.example .env
# Edita `.env` si necesitas cambiar puertos o credenciales
```

2. Construir y levantar todos los servicios:

```bash
docker compose up --build
```

3. Acceder desde el navegador:

- Generador: http://localhost:3000
- Usuario: http://localhost:5173
- Plantillas: http://localhost:8080
- Infraestructura (Nginx/static): http://localhost:80

Notas:
- Si tu proyecto necesita una base de datos, descomenta y ajusta la sección `db` en
	`docker-compose.yml` y completa los valores en `.env`.
- El `docker-compose.yml` usa variables de entorno con valores por defecto,
	por lo que el proyecto puede levantarse aun sin un `.env` si no necesitas
	cambiar los puertos por defecto.

Si quieres, puedo también:
- añadir un `healthcheck` más específico para cada servicio,
- o ejecutar `docker compose up` desde aquí para probar (necesitaría permiso).
