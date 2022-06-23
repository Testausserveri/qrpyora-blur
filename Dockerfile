FROM node:alpine

WORKDIR /home/app
COPY package.json package-lock.json main.py util.py server.js requirements.txt upload/* public/* /home/app/

RUN apk add python3 zbar && npm install && pip -r requirements.txt

EXPOSE 3000
CMD ["node", "server.js"]