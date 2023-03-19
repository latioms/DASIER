# dockerize my app.py and my models
FROM python:3.9-slim-buster

# working directory
WORKDIR /app

# run requirements
COPY requirements.txt /requirements.txt

COPY server/ .

COPY models /models

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
