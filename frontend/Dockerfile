FROM node:20.15-bullseye-slim

WORKDIR /frontend

COPY package.json package-lock.json ./
RUN npm install

COPY . /frontend/
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]