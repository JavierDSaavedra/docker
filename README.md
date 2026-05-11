
```bash
docker build -t generador ./Generador
docker build -t usuario ./Usuario
docker build -t plantillas ./Plantillas
docker build -t infraestructura "./Estructura institucional"

# ejecutar contenedores
docker run -d --name generador -p 3000:3000 generador
docker run -d --name usuario -p 5173:5173 usuario
docker run -d --name plantillas -p 8080:8080 plantillas
docker run -d --name infraestructura -p 80:80 infraestructura
```
# Docker - UBB

Proyecto: `Generador`, `Usuario`, `Plantillas` y `Estructura institucional` (Nginx).

Instrucciones rápidas:

1. Copia la plantilla de variables de entorno:

```bash
cp .env.example .env
```

2. Construir y levantar todos los servicios:

```bash
docker compose up --build
```

3. Acceder en el navegador:

- Generador: http://localhost:3000
- Usuario: http://localhost:5173
- Plantillas: http://localhost:8080
- Infraestructura (Nginx): http://localhost (puerto 80)

Detener y eliminar contenedores/recursos:

```bash
docker compose down
```
