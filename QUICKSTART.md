# ⚡ Quick Start

## 1. Build

```bash
# ⚡ Quick Start

## 1️⃣ Build

```bash
# Build images per service
docker build -t generador ./Generador
docker build -t usuario ./Usuario
docker build -t plantillas ./Plantillas
docker build -t infraestructura "./Estructura institucional"
```

## 2️⃣ Run

```bash
# Run containers
docker run -d --name generador -p 3000:3000 generador
docker run -d --name usuario -p 5173:5173 usuario
docker run -d --name plantillas -p 8080:8080 plantillas
docker run -d --name infraestructura -p 80:80 infraestructura
```

## 3️⃣ Access

- http://localhost:3000 (Generador)
- http://localhost:5173 (Usuario)
- http://localhost:8080 (Plantillas)
- http://localhost (Infraestructura)

## 4️⃣ Stop

```bash
docker stop generador usuario plantillas infraestructura
docker rm generador usuario plantillas infraestructura
```

## 📋 Comandos Útiles

```bash
docker-compose ps           # Ver estado
docker-compose logs -f      # Ver logs
docker-compose restart      # Reiniciar
docker-compose exec <svc> sh # Entrar en contenedor
```

## 🔗 Conectar Servicios

Todos están en red `app`, úsalos por nombre:

```
generador:3000
usuario:5173
plantillas:8080
infraestructura:80
```
