from userapp.models import User
from userapp.serializers import UserSerializer, UserAdminSerializer, UserAdminSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from auth.custom_permissions import IsModerator
from file_operations.operations import FileIO


# Create your views here.

class GetUserView(APIView):
    '''
    Class to GET all model User:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        GET a list of all users in system:
        '''
        if request.user.is_staff:
            queryset = User.objects.all()

            serialized = UserSerializer(queryset, many=True)

            return Response(
                serialized.data,
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(
                {
                    "error": "Unauthorized"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )


class AddUserView(APIView):
    '''
    Register a new user.
    '''

    def post(self, request):
        '''
        POST a new user to the system:
        '''
        data = request.data
        # print(f"\n\n\nPassword: {data['password']}\n\n\n")
        data['password'] = make_password(data.get('password'))

        if 'is_staff' in data.keys():
            data['is_staff'] = False
        if 'is_superuser' in data.keys():
            data['is_superuser'] = False
        if 'has_key' in data.keys():
            data['has_key'] = False
        if 'user_type' in data.keys():
            data['user_type'] = 'normal_user'

        deserialized = UserSerializer(data=data)

        if deserialized.is_valid():
            deserialized.save()
            return Response(
                {
                    "success": f"User: {deserialized.data.get('username')} created."
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "error": str(deserialized.errors)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginView(APIView):
    '''
    View to login a user and create their token:
    '''

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')
        # print(f"\n\n\nPassword: {password}\n\n\n")
        user = User.objects.filter(username=username).first()

        if user is None:
            return Response(
                {
                    "error": "Invalid Username"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(password, user.password):
            return Response(
                {
                    "error": "Invalid Password"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token = Token.objects.get_or_create(user=user)

        FileIO.write_token_to_file(username, token)

        return Response(
            {
                "token": str(token[0])
            },
            status=status.HTTP_202_ACCEPTED
        )


class UserLogoutView(APIView):
    '''
    View to logout user and destroy their token:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.filter(user=request.user).first()
        token.delete()

        return Response(
            {
                "success": "Logged Out."
            }
        )


class SetSuperView(APIView):
    '''
    Class to set superusers:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, slug: str):
        try:
            user = User.objects.get(user_slug=slug)
            if user.is_superuser:
                return Response(
                    {
                        "error": "user is already superuser."
                    },
                    status=status.HTTP_200_OK
                )
            user.is_superuser = True
            user.save()
            serialized = UserAdminSerializer(user)
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    "error": "User does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SetStaffView(APIView):
    '''
    Class to set superusers:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, slug: str):
        try:
            user = User.objects.get(user_slug=slug)
            if user.is_staff:
                return Response(
                    {
                        "error": "user is already staff."
                    },
                    status=status.HTTP_200_OK
                )
            user.is_staff = True
            user.save()
            serialized = UserAdminSerializer(user)
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {
                    "error": "User does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )


class UserGetView(APIView):
    '''
    API to get/delete details of a single user:
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug: str):
        '''
        Get a single user via ID:
        '''
        user_data = User.objects.get(user_slug=slug)

        if request.user == user_data or request.user.is_staff:
            serialized = UserAdminSerializer(user_data)
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        else:
            user_data = None
            return Response(
                {
                    "error": "Unauthorised access"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, slug: str):
        '''
        Delete a single user via slug:
        '''
        user_data = User.objects.get(user_slug=slug)

        if request.user == user_data or request.user.is_staff:
            serialized = UserAdminSerializer(user_data)
            user_data.delete()
            return Response(
                serialized.data,
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            user_data = None
            return Response(
                {
                    "error": "Unauthorised access"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class MakeModeratorView(APIView):
    '''
    API to assign a user as a moderator
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser, IsModerator)

    def post(self, request):
        '''
        POST request to assign a moderator
        '''
        target_user_slug = request.data.get("target_user_slug")
        target_user = User.objects.get(user_slug=target_user_slug)
        if target_user is None:
            raise User.DoesNotExist

        if target_user.user_type == "moderator":
            resp = {
                "error": "this user is already a moderator."
            }
            status_code = status.HTTP_406_NOT_ACCEPTABLE

        if target_user.user_type == "maintainence" or target_user.user_type == "user_admin":
            resp = {
                "warning": f"this user is of higher access: {target_user.user_type}"
            }
            target_user.user_type == "moderator"
            target_user.save()
            status_code = status.HTTP_202_ACCEPTED

        target_user.user_type == "moderator"
        target_user.save()
        status_code = status.HTTP_201_CREATED
        serialized = UserSerializer(target_user)

        resp = serialized.data

        return Response(
            resp,
            status_code
        )
