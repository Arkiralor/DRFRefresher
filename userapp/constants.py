import re

class UserRegex:
    """
    Class to hold regexes for User models in userapp.
    """

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    PHONE_REGEX_IN = re.compile(r'^[0-9]{10}$')
    PHONE_REGEX_US = re.compile(r'^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$')