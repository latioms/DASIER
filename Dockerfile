# dockerize my app.py and my models
FROM python:3.9

# working directory
WORKDIR /app

# run requirements
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY app.py /app.py

COPY models /models

CMD ["python", "app.py"]
