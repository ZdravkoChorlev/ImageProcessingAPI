FROM python:3.8

EXPOSE 8000

COPY . .

RUN pip install pipenv

RUN pip install psycopg2-binary

RUN pip install python-dotenv

RUN pip install validators

RUN pipenv install --system --dev