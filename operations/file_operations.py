from datetime import datetime
from constants.file_paths import FilePath
from operations import logger
from os import path, makedirs


class FileIO:
    """
    Class to handle file operations
    """

    @classmethod
    def create_if_not_exists(cls, path_name=None):
        """
        Creates a file/folder in the repository directory if it does not exist.  

        Keyword arguments:
        path_name: destination path to be checked.

            -> 201 | 200: status code for (created | found)
        """

        if not path.exists(path=path_name):
            makedirs(path_name)
            return 201
        return 200

    @classmethod
    def write_token_to_file(cls, username: str, token: str):
        """
        Writes the user's token to a .csv file upon login.

        Keyword arguments:
        username: name of the user who just logged in.
        token: token_value of the user who just logged in.

            -> None:
        """
        logger.info(f"Compiling output data for {username}'s authtoken.")

        #TODO: This file CRITICALLY needs to be untracked by the VC system.
        file_data = f"{datetime.now()}, {username}, {str(token[0])}\n"

        with open(FilePath.token_file, "a+t", encoding="utf-8")as token_csv:
            token_csv.write(file_data)
            logger.info(
                f"Stored {username}'s authtoken to {FilePath.token_file}.")
