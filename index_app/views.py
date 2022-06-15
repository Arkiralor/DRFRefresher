from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from os import environ

from index_app import logger
from userapp.models import User, UserProfile
from userapp.serializers import UserSearchSerializer, UserProfileSerializer

# Create your views here.


def index(request):
    """
    View to render the index page.
    """
    logger.info("Index page loaded.")
    resp_dict = {
        'title': 'Index',
        'welcome_message': 'Welcome to the index page.',
        'message': 'Please use the APIs to interface with the backend.',
        'linkedin_profile': environ.get('LINKEDIN_PROFILE', ''),
        'documentation': {
            'userapp_docs': environ.get('USERAPP_DOCS'),
            'locationapp_docs': environ.get('LOCATIONAPP_DOCS'),
            'storyapp_docs': environ.get('STORYAPP_DOCS'),
            'searchapp_docs': environ.get('SEARCHAPP_DOCS'),
        }
    }
    return render(
        request,
        template_name='index_app/index.html',
        context=resp_dict
    )


@login_required(login_url='/admin')  # redirect when user is not logged in
def see_users(request):
    """
    View to render the profile page.
    """
    logger.info("Profile page loaded.")

    users = User.objects.all().order_by('date_joined')

    context = {
        "users": users,
    }

    print(f"Response: {context}")

    return render(
        request,
        template_name='index_app/users.html',
        context=context
    )
