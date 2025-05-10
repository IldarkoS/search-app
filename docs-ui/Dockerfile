# docs-ui/Dockerfile
# ───────────────────────── build ─────────────────────────
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build           # dist/

# ───────────────────────── run ───────────────────────────
FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html

RUN printf '%s\n' "\
server {                                   \
  listen 80;                               \
  server_name _;                           \
                                           \
  root /usr/share/nginx/html;              \
  index index.html;                        \
                                           \
  location /api/ {                         \
    proxy_pass http://api-service:8000;    \
    proxy_set_header Host \$host;          \
    proxy_set_header X-Real-IP \$remote_addr; \
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for; \
    proxy_set_header X-Forwarded-Proto \$scheme; \
  }                                        \
                                           \
  location / {                             \
    try_files \$uri \$uri/ /index.html;    \
  }                                        \
}" > /etc/nginx/conf.d/default.conf
