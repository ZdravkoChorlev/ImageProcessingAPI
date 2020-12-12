import validators
import requests


def is_url_valid(self, url):
    valid = validators.url(url)

    return valid


def is_url_img(self, url):
    response = requests.head(url)
    content = response.headers.get('content-type')
    img_pattern = "image"

    return img_pattern in content
