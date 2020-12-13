import requests
import uvicorn

from image_processing import ProcessImage
from fastapi import FastAPI
from PIL import Image


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello"}


@app.post("/image")
def get_img_info(img_url):

    img = ProcessImage()
    dict_result = {}

    response = requests.get(img_url, stream=True)
    raw_img = response.raw

    img_blurhash = img.get_blurhash(raw_img)
    img_sha1 = img.get_sha1(response.content)
    img_dimensions = img.get_dimensions(img_url)
    img_type = img.get_type(response.headers)

    img_info = {"blurhash": img_blurhash, "sha1": img_sha1,
                "dimensions": img_dimensions, "type": img_type}

    return img_info


@ app.get("/retrieve")
def retrieve_imgs():
    return "Success"


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
