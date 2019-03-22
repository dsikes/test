FROM python:3.8.0a2-alpine3.9

MAINTAINER Dan Sikes <Daniel.Sikes@ge.com>

COPY ./app /app

RUN pip install -r /app/requirements.txt

RUN pip install gunicorn

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "run:app","--config", "/app/gunicorn.config.py"]