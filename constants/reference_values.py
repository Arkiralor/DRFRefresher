from constants import logger
from os import sep


class StringConstant:
    """
    Class to contain global string constants for the project.
    """
    logger.info("Initiating String Constants.")

    token_header = "token"
    at = "@"
    dot = "."
    hypen = "-"
    underscore = "_"
    slash = sep


class ProjectConstants:
    """
    Class to hold reference values for project.
    """
    LANG_DICT = {
        "am": "Amharic",
        "ar": "Arabic",
        "as": "Assamese",
        "bn": "Bengali",
        "bo": "Tibetan",
        "ca": "Catalan",
        "de": "German",
        "default": "Unknown",
        "en": "English",
        "es": "Spanish",
        "fa": "Persian",
        "fr": "French",
        "gu": "Gujarati",
        "hi": "Hindi",
        "id": "Indonesian",
        "is": "Icelandic",
        "it": "Italian",
        "ja": "Japanese",
        "km": "Khmer",
        "kn": "Kannada",
        "ko": "Korean",
        "lo": "Lao",
        "ml": "Malayalam",
        "mr": "Marathi",
        "ms": "Malay",
        "my": "Burmese",
        "ne": "Nepali",
        "no": "Norweigian",
        "or": "Oriya",
        "pa": "Punjabi",
        "pt": "Portuguese",
        "ru": "Russian",
        "sa": "Sanskrit",
        "sd": "Sindhi",
        "si": "Sinhala",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tl": "Tagalog",
        "tr": "Turkish",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "zh-cn": "Chinese"
    }


if __name__ == "__main__":
    pass
