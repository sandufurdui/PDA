
FROM node:18.12.1

WORKDIR /app

COPY package*.json ./

RUN npm install 

COPY . .

ENV PORT=5555

EXPOSE 5555

CMD [ "node", "app.js" ]