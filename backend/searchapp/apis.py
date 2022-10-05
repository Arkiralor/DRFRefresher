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
from userapp.serializers import UserSearchSerializer

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
            stories = Story.objects.filter(
                title__icontains=title).order_by('-created_at')
            results = StorySerializer(stories, many=True).data
        elif params.get('like', None):
            like = params.get('like')
            ## TODO: This needs to be offloaded to a messaging queue.
            results = SearchHelper.find_similiar(like)
        else:
            results = []
            return Response(
                {
                    'error': 'No search parameters provided.',
                    'results': results,
                }
            )

        resp = {
            'hits': len(results),
            'results': results,
            'query': dict(params),
            'requester': request.user.username,
            'searched_at': timestamp
        }

        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class AllStoriesByAuthorAPI(APIView):
    """
    API to retrieve all stories by a single author
    """

    def get(self, request):
        """
        GET method to get all stories by a single author
        """
        author = request.query_params.get('author')
        if not author:
            return Response(
                {
                    "error": "Please provide author"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        stories = Story.objects.filter(
            author__username=author).order_by('-created_at')
        if not stories:
            return Response(
                {
                    "error": f"No stories submitted by {author}"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serialized = StorySerializer(stories, many=True)
        return Response(
            serialized.data,
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
            users = User.objects.filter(
                username__icontains=username)
            results = UserSearchSerializer(users, many=True).data
        elif params.get('email', None):
            email = params.get('email')
            users = User.objects.filter(
                email__icontains=email)
            results = UserSearchSerializer(users, many=True).data
        else:
            results = User.objects.all().values("username")

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
