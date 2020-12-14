FROM python:3.8

EXPOSE 8000

COPY . .

RUN pip install pipenv

RUN pip install Hypercorn

COPY Pipfile Pipfile.lock /

RUN pipenv install --system --dev