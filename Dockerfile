# dockerize my app.py and my models
FROM python:3.9-slim-buster

# working directory
WORKDIR /app

# run requirements
COPY requirements.txt ./requirements.txt

COPY server/ .

COPY models /models

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
