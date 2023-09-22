FROM python:3.10-alpine AS builder
EXPOSE 5000
RUN apk update
RUN apk add pkgconfig
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt




COPY . .


RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]