"""
Write tests for this module.
"""
from constants.file_paths import FilePath

from unittest import TestCase
from os import path
from constants import logger
from core.settings import LOG_DIR, ENV_LOG_FILE, DJANGO_LOG_FILE


class TestIfPathsExist(TestCase):
    """
    Test if the paths exist.
    """
    module_name = __module__.split('.')[0]
    logger.info(f"Initiating tests for File Paths.")

    def test_if_token_exists(self):
        """
        Test if the file paths exist.
        """
        self.assertTrue(path.exists(FilePath.token_file))

    def test_if_sql_dump_exists(self):
        """
        Test if the file paths exist.
        """
        self.assertTrue(path.exists(FilePath.sql_dump_file))

    def test_if_log_dir_exists(self):
        """
        Test if the log directory exists.
        """
        self.assertTrue(path.exists(LOG_DIR))

    def test_if_env_log_file_exists(self):
        """
        Test if the log file exists.
        """
        self.assertTrue(path.exists(ENV_LOG_FILE))

    def test_if_django_log_file_exists(self):
        """
        Test if the log file exists.
        """
        self.assertTrue(path.exists(DJANGO_LOG_FILE))
