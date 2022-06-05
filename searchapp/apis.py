from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse  # Use this where response in broken.
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from storyapp.models import Story
from storyapp.serializers import StorySerializer
from searchapp.helpers import SearchHelper
from userapp.models import User
from userapp.serializers import UserSerializer

from datetime import datetime

class SearchStoryAPI(APIView):
    """
    API to search for stories.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        GET method to search for stories based on various parameters.

        params:
            'title' Optional
            'like' Optional
        """
        timestamp = datetime.now()
        params = request.query_params

        if params.get('title', None):
            title = params.get('title')
            stories = Story.objects.filter(title__icontains=title).order_by('-created_at')
            results = StorySerializer(stories, many=True).data
        elif params.get('like', None):
            like = params.get('like')
            results = SearchHelper.find_similiar(like)
        else:
            stories = Story.objects.all().order_by('-created_at')
            results = StorySerializer(stories, many=True).data

        resp = {
            'results': results,
            'query': params,
            'requester': request.user.username,
            'searched_at': timestamp
        }

        return Response(
            data=resp,
            status=status.HTTP_200_OK
        )


class SearchUserAPI(APIView):
    """
    API to search for users.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        GET method to search for users based on various parameters.

        params:
            'username' Optional
            'email' Optional
        """
        timestamp = datetime.now()
        params = request.query_params

        if params.get('username', None):
            username = params.get('username')
            users = User.objects.filter(username__icontains=username).order_by('-created_at')
            results = UserSerializer(users, many=True).data
        elif params.get('email', None):
            email = params.get('email')
            users = User.objects.filter(email__icontains=email).order_by('-created_at')
            results = UserSerializer(users, many=True).data
        else:
            users = User.objects.all().order_by('-created_at')
            results = UserSerializer(users, many=True).data

        resp = {
            'results': results,
            'query': params,
            'requester': request.user.username,
            'searched_at': timestamp
        }

        return Response(
            data=resp,
            status=status.HTTP_200_OK
        )


