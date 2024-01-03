FROM node:latest

COPY package*.json .
RUN npm install --force
COPY . /home/app/frontend/.
WORKDIR /home/app/frontend
RUN npm run build

