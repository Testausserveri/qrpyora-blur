FROM node:alpine

WORKDIR /home/app
COPY package.json package-lock.json main.py util.py server.js requirements.txt upload/* public/* /home/app/

RUN apt install python3 python3-pip zbar && npm install

EXPOSE 3000
CMD ["node", "server.js"]