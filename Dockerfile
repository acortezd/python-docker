FROM python:3.7.3-alpine3.8

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install -U flask-cors

ENTRYPOINT ["python"]
CMD ["main.py"]