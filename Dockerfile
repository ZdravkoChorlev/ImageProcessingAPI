FROM python:3.8-alpine

EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt

RUN python main.py
