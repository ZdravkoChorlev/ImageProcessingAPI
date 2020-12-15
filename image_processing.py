import requests
import hashlib
import blurhash
import logging

from io import BytesIO
from PIL import Image

logging.basicConfig(filename='error.log', level=logging.DEBUG)


class ProcessImage():
    """
        The ProcessImage class handles processing of image by given URL 
    """

    def get_sha1(self, content):
        """ Extracts image's sha1 code from HTTP request

            Params:
                content (str): HTTP request content
            Returns:
                sha1_code(str) of the image in hexdecimal form
        """
        try:
            sha1_code = hashlib.sha1(content)
        except Exception as error:
            logging.error("Cannot get sha1: ", error)
            return None

        return sha1_code.hexdigest()

    def get_blurhash(self, resp_raw):
        """Extracts image's blurhash from HTTP request

        Parameters:
            resp_raw (Response): raw response of the request

        Returns:
            int: blurhash of the image
        """
        blurhash_code = blurhash.encode(
            resp_raw, x_components=4, y_components=5)

        return blurhash_code

    def get_type(self, resp_headers):
        """Extracts image type from HTTP request

        Parameters:
            resp_headers (MuttableMapping): headers of request

        Returns:
            str: the type of the image
        """
        content_type = ''
        img_type = ''
        try:
            content_type = resp_headers.get('content-type')
            img_type = content_type.split('/')[1]
        except Exception as error:
            logging.error("Cannot get headers from request: ", error)
            return None

        return img_type

    def get_dimensions(self, img_url):
        """Extracts image dimensions from HTTP request

        Parameters:
            img_url (str): URL of the image

        Returns:
            list: width and height of the image
        """
        resp = requests.get(img_url)
        content = resp.content
        try:
            img = Image.open(BytesIO(content))
            width, height = img.size
        except IOError as error:
            logging.error("Cannot open image: ", error)
            return None

        return width, height
