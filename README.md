# Docker - UBB

4 microservicios conectados en una red simple.

## 🚀 Iniciar

```bash
# Construir imágenes (una por servicio)
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

# Logs de un servicio
docker-compose logs -f generador

# Reiniciar
docker-compose restart

# Entrar en contenedor
docker-compose exec generador sh
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
├── docker-compose.yml
├── README.md
├── QUICKSTART.md
├── .env.example
└── .gitignore
```
