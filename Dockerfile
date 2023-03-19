# dockerize my app.py and my models
FROM python:3.9-slim-buster

# working directory
WORKDIR /app

COPY server/ .

# run requirements
COPY ./requirements.txt /app

# Installation des dépendances
RUN pip install --no-cache-dir flask 

COPY models /models

EXPOSE 5000

CMD ["python", "app.py"]
