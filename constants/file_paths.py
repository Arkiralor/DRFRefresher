from os import path
from core.settings import BASE_DIR

class FilePath:
    token_file = path.join(BASE_DIR, "temp", "tokens.csv")