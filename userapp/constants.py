import re


class UserRegex:
    """
    Class to hold regexes for User models in userapp.
    """

    # 'john.doe@email.com'
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    PHONE_REGEX_IN = re.compile(r'^[0-9]{10}$')  # 9864049831
    # prithoo: I don't know what the format is; I just copied this from the internet.
    PHONE_REGEX_US = re.compile(r'^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$')
    # 1 UC char, 1 LC char, 1 NUM char; between 8 to 15 chars
    PASSWORD_REGEX = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,15}$')
