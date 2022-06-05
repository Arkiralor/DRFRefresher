from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse  # Use this where response in broken.
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from storyapp.models import Story
from storyapp.serializers import StorySerializer
from datetime import datetime


class GetAllStoriesAPI(APIView):
    """
    API class to get all stories in system.
    """

    def get(self, request):
        """
        GET method to get all stories in system
        """
        stories = Story.objects.all()
        serialized = StorySerializer(stories, many=True)
        resp = {
            "hits": serialized.data,
            "total": len(serialized.data),
            "requested_at": datetime.now()
        }
        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class AddStoryAPI(APIView):
    """
    API class to add a new story to system.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        POST method to add a new story to system
        """
        serialized = StorySerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serialized.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class IndividualStoryAPI(APIView):
    """
    API class to get a single story.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        GET method to get a single story.
        """
        # Get query parameters
        story_id = request.query_params.get('story_id')
        story_slug = request.query_params.get('story_slug')

        if story_id and not story_slug:
            story = Story.objects.get(id=story_id)
            identifier = story_id
        elif story_slug and not story_id:
            story = Story.objects.get(slug=story_slug)
            identifier = story_slug
        else:
            return Response(
                {
                    "error": "Please provide either story_id or story_slug"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not story:
            return Response(
                {
                    "error": f"Story with identifier {identifier} not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serialized = StorySerializer(story)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        """
        PUT method to update a single story.
        """
        # Get query parameters
        story_id = request.query_params.get('story_id')
        story_slug = request.query_params.get('story_slug')

        if story_id and not story_slug:
            story = Story.objects.get(id=story_id)
            identifier = story_id
        elif story_slug and not story_id:
            story = Story.objects.get(slug=story_slug)
            identifier = story_slug
        else:
            return Response(
                {
                    "error": "Please provide either story_id or story_slug"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not story:
            return Response(
                {
                    "error": f"Story with identifier {identifier} not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if story.author != request.user and not request.user.is_superuser:
            return Response(
                {
                    "error": f"You are not authorized to update this story"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serialized = StorySerializer(story, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serialized.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        """
        DELETE method to delete a single story.
        """
        identifier = None
        # Get query parameters
        story_id = request.query_params.get('story_id')
        story_slug = request.query_params.get('story_slug')

        if story_id and not story_slug:
            story = Story.objects.get(id=story_id)
            identifier = story_id
        elif story_slug and not story_id:
            story = Story.objects.get(slug=story_slug)
            identifier = story_slug
        else:
            return Response(
                {
                    "error": "Please provide either story_id or story_slug"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not story:
            return Response(
                {
                    "error": f"Story with identifier {identifier} not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        story.delete()
        return Response(
            {
                "message": f"Story with identifier {identifier} deleted successfully"
            },
            status=status.HTTP_200_OK
        )
