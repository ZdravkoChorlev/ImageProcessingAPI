FROM python:3.8

EXPOSE 8000

COPY . .

RUN pip install pipenv

RUN pipenv install --system --dev