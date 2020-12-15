"""
This module contains some functions that are useful for image processing
"""
import requests
import validators
import urllib.parse


def is_url_valid(url):
    """Validates given URL

    Params:
        url(str): URL

    Returns:
        bool: returns true if the url is valid, otherwise return result is false
    """
    valid = validators.url(url)

    return valid


def is_url_img(url):
    """Checks if given URL is an image

    Params:
        url(str): URL

    Returns:
        bool: returns true if the URL is an image, otherwise return result is false
    """
    response = requests.head(url)
    content = response.headers.get('content-type')
    img_pattern = "image"

    return img_pattern in content


def resize_url(url):
    """ Concatenates URL with fixed dimensions for better permormance of processing the content of the URL

    Params:
        url (str): URL
    Returns:
        (str): the resized URL
    """
    resize_pattern = "?width=10&height=10"
    resized_url = urllib.parse.urljoin(url, resize_pattern)

    return resized_url
