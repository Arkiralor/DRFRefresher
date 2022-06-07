from django.shortcuts import render

from index_app import logger

# Create your views here.

def index(request):
    """
    View to render the index page.
    """
    logger.info("Index page loaded.")
    resp_dict = {
            'title': 'Index',
            'welcome_message': 'Welcome to the index page.',
            'message': 'Please use the APIs to interface with the backend.'
        }
    return render(
        request, 
        template_name='index_app/index.html',
        context=resp_dict
    )
