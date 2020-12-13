import requests
import hashlib
import blurhash

from io import BytesIO
from PIL import Image


class ProcessImage():

    def get_sha1(self, img_name):
        h = hashlib.sha1(img_name)

        return h.hexdigest()

    def get_blurhash(self, resp_raw):
        blur_hash = blurhash.encode(resp_raw, x_components=4, y_components=3)

        return blur_hash

    def get_type(self, resp_headers):
        content_type = resp_headers.get('content-type')
        img_type = content_type.split('/')[1]

        return img_type

    def get_dimensions(self, img_url):
        resp = requests.get(img_url)
        content = resp.content

        img = Image.open(BytesIO(content))
        width, height = img.size

        return width, height
