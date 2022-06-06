from os import path, sep
from core.settings import BASE_DIR


class FilePath:
    """
    Class to contain global file paths for the project.
    """
    token_file = path.join(BASE_DIR, "temp", "tokens.csv")


class StringConstant:
    """
    Class to contain global string constants for the project.
    """
    token_file_header = "token"
    at = "@"
    dot = "."
    slash = sep

