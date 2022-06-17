from os import path, makedirs, environ
from core.settings import BASE_DIR
from constants import logger


class FilePath:
    """
    Class to contain global file paths for the project.
    """
    logger.info("Initiating File Paths.")
    temp_files_dir = path.join(BASE_DIR, "temp")
    sql_dump_dir = path.join(BASE_DIR, temp_files_dir, "SQLDump")
    if not path.exists(temp_files_dir):
        makedirs(temp_files_dir)

    if not path.exists(sql_dump_dir):
        makedirs(sql_dump_dir)
    
    token_file = path.join(BASE_DIR, temp_files_dir, "tokens.csv")
    sql_dump_file = path.join(BASE_DIR, temp_files_dir, sql_dump_dir, f"{environ.get('PGDATABASE')}.sql")

    
    def __init__(self):

        pass



if __name__ == "__main__":
    pass
