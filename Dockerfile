FROM python:3.8

WORKDIR /home/app
COPY package.json package-lock.json main.py util.py server.js requirements.txt upload/* public/* /home/app/

RUN apt install nodejs npm zbar && npm install && pip install -r requirements.txt

EXPOSE 3000
CMD ["node", "server.js"]