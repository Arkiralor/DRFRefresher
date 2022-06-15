
from auth.custom_permissions import IsModerator
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token

from blacklist.utils import banned_passwords, banned_emails, banned_phone_numbers
from operations.file_operations import FileIO
from userapp.helpers import EmailHelper, OTPHelper
from userapp import logger
from userapp.models import User, UserProfile, UserOTP
from userapp.serializers import UserSerializer, UserAdminSerializer, UserAdminSerializer, UserProfileSerializer, LoginSerializer
from userapp.constants import UserRegex


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
            queryset = User.objects.all().order_by('date_joined')

            serialized = UserAdminSerializer(queryset, many=True)

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

        data:
            username: str
            email: str
            password: str
            first_name: Optional[str]
            last_name: Optional[str]
            user_phone_primary: Optional[str]
        '''
        data = request.data

        if not data.get('username') or not data.get('password') or not data.get('email'):
            return Response(
                {
                    "error": "USERNAME, PASSWORD and EMAIL are MANDATORY"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(data.get('username')) == 0 or len(data.get('password')) == 0 or len(data.get('email')) == 0:
            return Response(
                {
                    "error": "USERNAME, PASSWORD and EMAIL are MANDATORY"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        ## Make sure that a banned user is not trying to get back in.
        if data.get('email') in banned_emails():
            return Response(
                {
                    "error": "Whoa! Whoa there, buddy! You know you're not allowed back in here after what you pulled!"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        ## Make sure that a banned user is not trying to get back in.
        if 'user_phone_primary' in data.keys() and data.get('user_phone_primary') in banned_phone_numbers():
            return Response(
                {
                    "error": "Whoa! Whoa there, buddy! You know you're not allowed back in here after what you pulled!"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        ## Make sure that the user is not setting up a STUPID password.
        if data.get('password') in banned_passwords():
            return Response(
                {
                    "error": "Really, bro/sis? You could've used a better password. Get back to me when you come up with a better one."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        # prrithoo: We are validating the password here because we cannot do that once the password
        # has been hashed and salted.
        if not UserRegex.PASSWORD_REGEX.search(data.get('password')):
            return Response(
                {
                    "error": "Password MUST contain 1 UPPERCASE character, 1 lowercase character and 1 numerical character."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data['password'] = make_password(data.get('password'))

        # Sanitizing request data
        if 'is_staff' in data.keys():
            data['is_staff'] = False
        if 'is_superuser' in data.keys():
            data['is_superuser'] = False
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


class UserLoginView(GenericAPIView):
    '''
    View to login a user and create their token:
    '''
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')
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

    def put(self, request, slug: str):
        '''
        Update a single user via ID:
        '''
        user_data = User.objects.get(user_slug=slug)

        if request.user == user_data or request.user.is_staff:
            data = request.data
            serialized = UserAdminSerializer(user_data, data=data)

            if serialized.is_valid():
                serialized.save()
                return Response(
                    {
                        "success": f"User: {serialized.data.get('username')} updated."
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "error": str(serialized.errors)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
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


class GetAllProfilesAPI(APIView):
    '''
    API to get all profiles
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get(self, request):
        '''
        GET request to get all profiles
        '''
        profiles = UserProfile.objects.all()
        serialized = UserProfileSerializer(profiles, many=True)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )


class UserLoginOTPAPI(APIView):
    """
    API to generate OTP and send it to the user's email.
    """

    def post(self, request):
        """
        POST request to generate OTP and send it to the user's email.
        """
        data = request.data
        username = data.get("username")
        email = data.get("email")

        if not username and not email:
            return Response(
                {
                    "error": "username or email is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(
            Q(username=username)
            & Q(email=email)
        ).first()

        if not user:
            return Response(
                {
                    "error": f"User '{username}' with the email '{email}' does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        otp = OTPHelper.generate_otp()
        hashed_otp = make_password(otp)

        user_otp = UserOTP.objects.filter(user=user).first()

        ## If user has already generated OTP, delete the old OTP.
        if user_otp:
            user_otp.delete()
            user_otp = None

        user_otp = UserOTP.objects.create(
            user=user,
            otp=hashed_otp
        )
        user_otp.save()

        EmailHelper.send_otp_email(user, otp)

        return Response(
            {
                "message": f"OTP generated for user: {username} and sent to {user.email}",
            },
            status=status.HTTP_201_CREATED
        )


class UserValidateOTPAPI(APIView):
    """
    API to validate OTP.
    """

    def post(self, request):
        """
        POST request to validate OTP.
        """
        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            return Response(
                {
                    "error": "email AND otp are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user_otp = UserOTP.objects.filter(user__email=email).last()

        if not user_otp:
            return Response(
                {
                    "error": f"OTP for user '{email}' does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if OTP is expired:
        if timezone.now() > user_otp.expiry:
            user_otp.delete()
            return Response(
                {
                    "error": "OTP has expired. Generate a new OTP."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(otp, user_otp.otp):
            return Response(
                {
                    "error": "Invalid OTP"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email=email).first()

        token = Token.objects.get_or_create(user=user)

        FileIO.write_token_to_file(user.username, token)
        logger.info(f"OTP validated for user: {user.username}")
        user_otp.delete()

        return Response(
            {
                "token": str(token[0])
            },
            status=status.HTTP_202_ACCEPTED
        )
