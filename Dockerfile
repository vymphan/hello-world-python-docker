FROM python:latest

WORKDIR /usr/src/app

COPY ./main.py ./

CMD [ "python", "main.py" ]
