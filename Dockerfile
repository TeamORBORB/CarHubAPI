FROM python:alpine3.17

WORKDIR /carbackend
COPY . /carbackend

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

ENV GUNICORN_CMD_ARGS="--workers=1 --bind=127.0.0.1:8069"

EXPOSE 8069

CMD [ "gunicorn", "main:app" ]
