FROM python:alpine3.7
RUN apk --no-cache update && apk --no-cache add expat=2.2.7-r1

RUN apk update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]