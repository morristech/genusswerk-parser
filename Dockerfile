from python:3.7.5-slim-buster

RUN apt-get update
RUN apt-get install -y libgtk2.0-dev python3-tk ghostscript 

RUN pip install camelot-py[cv] matplotlib slackclient

WORKDIR /usr/src/genusswerkbot
COPY . .

ENTRYPOINT ["python", "/usr/src/genusswerkbot/genusswerkparser.py"]
