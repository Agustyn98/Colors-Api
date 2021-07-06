FROM python:alpine3.7

RUN apk update && apk add --no-cache gcc g++ python3-dev unixodbc-dev

RUN pip install --upgrade pip

WORKDIR /app

COPY .  /app/

RUN pip install -r requirements.txt

CMD ["python3","src/router.py"]