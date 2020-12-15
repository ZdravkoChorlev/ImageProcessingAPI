"""
API for image processing
"""
import requests
import uvicorn
import database
import logging

from utilities import is_url_valid, is_url_img, resize_url
from image_processing import ProcessImage
from database import Database
from fastapi import FastAPI
from PIL import Image


INFO_MSG = "This is simple web API for image processing v. 1.0.0"
NOT_IMG_MSG = "The URL does not contain image"
WRONG_URL_MSG = "The URL is wrong"

app = FastAPI()
logging.basicConfig(filename='error.log', level=logging.DEBUG)


@app.get("/")
def index():
    """ This is default endpoint. It gives info for the API
    """
    return INFO_MSG


@app.get("/image")
def get_img_info(img_url):
    """ This endpoint takes URL as param and returns image
     information(sha1 code, dimensions, type and blurhash) as JSON format

    Parameters:
        img_url(str): URL of the image
    Returns:
        (json): information about the image as JSON
    """
    img = ProcessImage()
    db = Database()
    img_info = {}

    if not is_url_valid(img_url):
        logging.error('Wrong URL', img_url)
        return WRONG_URL_MSG

    if not is_url_img(img_url):
        logging.error('Wrong image URL', img_url)
        return NOT_IMG_MSG

    resized_url = resize_url(img_url)

    response = requests.get(resized_url, stream=True)
    raw_img = response.raw

    img_blurhash = img.get_blurhash(raw_img)
    img_sha1 = img.get_sha1(response.content)
    img_dimensions = img.get_dimensions(img_url)
    img_type = img.get_type(response.headers)

    img_info = {"blurhash": img_blurhash, "sha1": img_sha1,
                "dimensions": img_dimensions, "type": img_type}

    conn = db.connect()
    if (conn):
        db.insert_data(img_info, conn)

    return img_info


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
