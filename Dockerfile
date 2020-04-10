FROM python:alpine3.7

RUN apk update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]