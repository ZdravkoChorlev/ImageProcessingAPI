import requests
import hashlib
import blurhash
import logging

from io import BytesIO
from PIL import Image

logging.basicConfig(filename='error.log', level=logging.DEBUG)


class ProcessImage():
    def get_sha1(self, img_name):
        try:
            h = hashlib.sha1(img_name)
        except Exception as error:
            logging.error("Cannot get sha1: ", error)

        return h.hexdigest()

    def get_blurhash(self, resp_raw):
        x_components = 4
        y_components = 3
        try:
            blur_hash = blurhash.encode(
                resp_raw, x_components=x_components, y_components=y_components)
        except Exception as error:
            logging.error("Cannot get blurhash: ", error)

        return blur_hash

    def get_type(self, resp_headers):
        try:
            content_type = resp_headers.get('content-type')
            img_type = content_type.split('/')[1]
        except Exception as error:
            logging.error("Cannot get headers from request: ", error)

        return img_type

    def get_dimensions(self, img_url):
        resp = requests.get(img_url)
        content = resp.content
        try:
            img = Image.open(BytesIO(content))
            width, height = img.size
        except IOError as error:
            logging.error("Cannot open image: ", error)

        return width, height
