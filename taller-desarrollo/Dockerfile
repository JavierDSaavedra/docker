# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the app
RUN npm run build

# Production stage - serve with Node + simple HTTP server
FROM node:20-alpine

WORKDIR /app

# Install http-server to serve static files
RUN npm install -g http-server

# Copy built files from builder
COPY --from=builder /app/dist ./dist

EXPOSE 5173

# Start http-server
CMD ["http-server", "dist", "-p", "5173"]
