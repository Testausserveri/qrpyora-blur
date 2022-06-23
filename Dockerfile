FROM python:3.8

WORKDIR /home/app
COPY package.json package-lock.json main.py util.py server.js requirements.txt upload/* public/* /home/app/

RUN apt-get update && apt-get install nodejs npm libzbar0 && npm install && pip install -r requirements.txt

EXPOSE 3000
CMD ["node", "server.js"]