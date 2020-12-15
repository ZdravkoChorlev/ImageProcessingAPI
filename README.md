# ImageProcessingAPI

This is simple web API for image processing created as example task from Scaleflex

The API purpose is to extract information(blurhash, sha1, type and dimensions) of given image by URL.
The application is working as docker-compose, it contains three containers: postgres database container, application container and pgadmin client container.

## Usage

Steps how to setup the API and to use it on your local computer

**Note**
You must have installed docker, docker-compose, python version >= 3.8, pipenv/pip

1. Checkout the git repository

2. Create .env file in the repository directory where the credentials for postgres database will be stored
    - It must contains the credentials fo PostgreSQL server and PgAdmin Client:
     ```POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        POSTGRES_DB=imageapi
        PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
        PGADMIN_DEFAULT_PASSWORD=admin
    ``` 

3. Create error.log and db_error.log files

4. Run `pip freeze > requirements.txt`
4. Run `docker-compose up` command

## Available Endpoints

When the docker compose is running we can access the functionality of the API
We have three available endpoints

1. `localhost:8000/` - This is default endpoint. It gives the user basic info the API

2. `localhost:8000/image?img_url=` - This is the main endpoint. Here we can pass a URL and get information about an image
    - Example:
    `localhost:8000/image?img_url=http://someurlimage.com"`

    - The output will be blurhash, sha1 code, type and dimensions(width, height) of the image in JSON format

3. `localhost:5050/` - This is PgAdmin client UI. Here we can get information about the data in the database and get the saved data
Example:
    - You need to login in the client UI by the given credentials in .venv and connect to postgres server