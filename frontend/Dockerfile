# Build do react - para gerar as páginas estáticas
FROM node AS build-stage
WORKDIR /home/app/static/nextjs
COPY . /home/app/static/nextjs/.
RUN npm install
RUN npm run build


FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /home/app/static/nextjs/.next /usr/share/nginx/html/.
RUN echo "<h3>Frontend in construction. Follow the endpoint '/api' for documentation</h3>" > /usr/share/nginx/html/index.html

