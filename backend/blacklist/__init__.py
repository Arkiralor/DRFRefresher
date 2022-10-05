"""
This app mainly deals with blacklisted values in the system:
    Story Tiles, Bodies
    User Names, Emails, Phone Numbers, Passwords, etc.
"""
import logging

logger = logging.getLogger('drf_logger.' + __name__)
default_app_config = 'index_app.apps.class BlacklistConfig'
