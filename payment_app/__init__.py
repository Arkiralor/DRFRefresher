"""
Initialize the logger for the application.
"""
import logging

logger = logging.getLogger('drf_logger.' + __name__)
default_app_config = 'payment_app.apps.PaymentAppConfig'
