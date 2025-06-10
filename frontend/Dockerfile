FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

RUN chmod +x node_modules/.bin/react-scripts
RUN npm run build

CMD ["npm", "start"]
