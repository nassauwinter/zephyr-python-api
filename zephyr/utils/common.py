"""Common helper functions to use with the package"""
from copy import deepcopy


def cookie_str_to_dict(cookie_str: str) -> dict:
    """
    Function to convert a cookie string from a browser Jira session to cookie dict for auth

    :param cookie_str: a string copied from Jira session in browser
    :returns: dict with parsed cookies
    """
    cookie_dict = {}
    for cookie_substr in cookie_str.split(";"):
        _key, _value = cookie_substr.strip().split("=", maxsplit=1)
        cookie_dict.update({_key: _value})
    return cookie_dict


def dict_merge(source, overwrite):
    """Recursively merges 2 dictionaries and return the merged dictionary"""
    result = deepcopy(source)
    for key, val in overwrite.items():
        if key in result and isinstance(result[key], dict):
            result[key] = dict_merge(result[key], val)
        else:
            result[key] = deepcopy(val)
    return result
