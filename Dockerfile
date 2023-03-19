# dockerize my app.py and my models
FROM python:3.9-slim-buster

# working directory
WORKDIR /app

# Copying the whole app
COPY . /app

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Running the setup file
RUN python setup.py install

EXPOSE 5000

# Running the app
CMD ["python", "server/app.py"]

