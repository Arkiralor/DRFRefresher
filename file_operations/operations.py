from datetime import datetime
from constants.file_paths import FilePath
from file_operations import logger


class FileIO:
    """
    Class to handle file operations
    """

    @classmethod
    def write_token_to_file(cls, username:str, token:str):
        logger.info(f"Compiling output data for {username}'s authtoken.")
        file_data = f"{datetime.now()}, {username}, {str(token[0])}\n"
        with open(FilePath.token_file, "a+t", encoding="utf-8")as token_csv:
            logger.info(f"Writing {username}'s authtoken to {FilePath.token_file}.")
            token_csv.write(file_data)