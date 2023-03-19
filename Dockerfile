# dockerize my app.py and my models
FROM python:3.9

# working directory
WORKDIR /app

# run requirements
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY server/* .

COPY models /models

CMD ["python", "app.py"]
