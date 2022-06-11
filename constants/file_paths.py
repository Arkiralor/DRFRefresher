from os import path, sep, environ
from core.settings import BASE_DIR
from constants import logger


class FilePath:
    """
    Class to contain global file paths for the project.
    """
    logger.info("Initiating File Paths.")
    token_file = path.join(BASE_DIR, "temp", "tokens.csv")
    sql_dump_file = path.join(
        BASE_DIR, "temp", "SQLDump", f"{environ.get('PGDATABASE')}.sql")


if __name__ == "__main__":
    pass
