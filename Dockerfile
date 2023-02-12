FROM python:3.7-slim-buster
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "encoder.py" ]
