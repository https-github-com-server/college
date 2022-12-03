FROM python:3.8-alpine
ENV LISTEN_PORT=5000
EXPOSE 5000
WORKDIR /server-college

ADD . /server-college/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt



CMD [ "python","main.py" ]

