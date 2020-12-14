import requests
import validators


def is_url_valid(url):
    valid = validators.url(url)

    return valid


def is_url_img(url):
    response = requests.head(url)
    content = response.headers.get('content-type')
    img_pattern = "image"

    return img_pattern in content
