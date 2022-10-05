from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

from blacklist.utils import banned_passwords, banned_emails, banned_phone_numbers
from core.settings import OTP_ATTEMPT_LIMIT, OTP_ATTEMPT_TIMEOUT
from operations.file_operations import FileIO
from userapp.helpers import EmailHelper, OTPHelper
from userapp import logger
from userapp.models import User, UserProfile, UserOTP
from userapp.serializers import UserSerializer, UserAdminSerializer, UserAdminSerializer, UserProfileSerializer, LoginSerializer
from userapp.constants import UserRegex

from datetime import timedelta



class GetUserView(APIView):
    '''
    Class to GET all model User:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

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

        ## Checking if the mandatory fields are Null:
        if not data.get('username') or not data.get('password') or not data.get('email'):
            return Response(
                {
                    "error": "USERNAME, PASSWORD and EMAIL are MANDATORY"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        ## Checking if the mandatory fields are blank:
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
    View to login a user with a username and password and create their token:
    '''
    serializer_class = LoginSerializer

    MAX_ATTEMPTS = OTP_ATTEMPT_LIMIT
    USER_TIMEOUT = OTP_ATTEMPT_TIMEOUT

    def post(self, request):
        """
        POST request handler to endpoint.

        request.data:
            username: str
            password: str
        """
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
        
        ## Checking if user is blocked
        if user.blocked_until and timezone.now() < user.blocked_until:
            return Response(
                {
                    "error": f"User '{username}' is blocked until {user.blocked_until}."
                },
                status=status.HTTP_403_FORBIDDEN
            )
        elif user.blocked_until and timezone.now() >= user.blocked_until:
            user.blocked_until = None
            user.save()

        if not check_password(password, user.password):
            user.unsuccessful_login_attempts += 1
            user.save()

            if user.unsuccessful_login_attempts >= self.MAX_ATTEMPTS:
                user.blocked_until = timezone.now() + timedelta(minutes=self.USER_TIMEOUT)
                user.unsuccessful_login_attempts = 0
                user.save()

                return Response(
                    {
                        "error": f"User '{username}' has been blocked for {self.USER_TIMEOUT} minutes, until {user.blocked_until}."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
            return Response(
                {
                    "error": "Invalid Password",
                    "message": f"You have {self.MAX_ATTEMPTS - user.unsuccessful_login_attempts} attempts remaining."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token = Token.objects.get_or_create(user=user)

        ## Resetting the Login attempt data if login is successfull:
        user.blocked_until = None
        user.unsuccessful_login_attempts = 0
        user.save()

        FileIO.write_token_to_file(username, token)

        return Response(
            {
                "status": True,
                'user_id': user.id, 
                'username': user.username,
                'first_name': user.first_name, 
                'last_name': user.last_name, 
                'email': user.email,
                "token": str(token[0]),
            },
            status=status.HTTP_202_ACCEPTED,
            headers=self.headers,
            content_type="application/json"
        )


class UserLogoutView(APIView):
    '''
    View to logout user and destroy their token:
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        POST request handler to endpoint.

        request.headers:
            Authorization: "token <string>"

        request.data:
            None
        """
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

class GetUserProfileAPI(APIView):
    """
    API endpoint to get a single user's profile
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, slug):
        """
        GET request handler to endpoint.

        request.headers:
            Authorization: "token <string>"

        request.data:
            None
        """
        user_profile = UserProfile.objects.get(user__user_slug=slug)
        serialized = UserProfileSerializer(user_profile)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )


class GetOwnUserProfileAPI(APIView):
    """
    API endpoint to edit a single user's profile
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        GET request handler to endpoint.

        request.headers:
            Authorization: "token <string>"

        request.data:
            None
        """
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        serialized = UserProfileSerializer(user_profile)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        """
        PUT request handler to endpoint.

        request.headers:
            Authorization: "token <string>"

        request.data:
            profile_picture: Optional[str]
            headline: Optional[str]
            bio: Optional[str]
            location: Optional[location]
        """
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        data = request.data
        serialized = UserProfileSerializer(user_profile, data=data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                {
                    "success": f"Profile: {serialized.data.get('user__username')} updated."
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



class GenerateUserLoginOTPAPI(APIView):
    """
    API to generate OTP and send it to the user's email.
    """
    MAX_OTP_ATTEMPTS = OTP_ATTEMPT_LIMIT
    USER_TIMEOUT = OTP_ATTEMPT_TIMEOUT

    def post(self, request):
        """
        POST request to generate OTP and send it to the user's email.
        """
        data = request.data
        username = data.get("username")
        email = data.get("email")

        if not username or not email:
            return Response(
                {
                    "error": "username and email is required."
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
        
        ## Checking if user is blocked
        if user.blocked_until and timezone.now() < user.blocked_until:
            return Response(
                {
                    "error": f"User with the email '{email}' is blocked until {user.blocked_until}."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        elif user.blocked_until and timezone.now() >= user.blocked_until:
            user.blocked_until = None
            user.save()

        ## Generate an OTP and generate a hash for the OTP:
        otp = OTPHelper.generate_int_otp()
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

        if settings.DEBUG or settings.ENV_TYPE == "dev":
            return Response(
                {
                    "message": "Sending OTP in Response.json() as Development Environment settings are activated.",
                    "OTP": otp,
                    "generating_user": user.username,
                    "generated_at": timezone.now()
                }
            )

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

    MAX_OTP_ATTEMPTS = OTP_ATTEMPT_LIMIT
    USER_TIMEOUT = OTP_ATTEMPT_TIMEOUT

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type/JSON",
        "Access-Control-Max-Age": "86400",
    }

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

        user_obj = User.objects.get(email=email)
        
        if not user_obj:
            return Response(
                {
                    "error": f"User with the email '{email}' does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
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

        ## Check if OTP is valid for the requesting user:
        if not check_password(otp, user_otp.otp):
            user_obj.unsuccessful_login_attempts += 1
            user_obj.save()

            ## If the number of unsuccessful login attempts is exceeds the limit, block the user;
            ## then, delete their OTP
            if user_obj.unsuccessful_login_attempts >= self.MAX_OTP_ATTEMPTS:
                user_obj.blocked_until = timezone.now() + timedelta(minutes=self.USER_TIMEOUT)
                user_obj.unsuccessful_login_attempts = 0
                user_obj.save()

                user_otp.delete()

                return Response(
                    {
                        "error": f"User '{email}' has been blocked for {self.USER_TIMEOUT} minutes, until {user_obj.blocked_until}."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            return Response(
                {
                    "error": "Invalid OTP",
                    "message": f"You have {self.MAX_OTP_ATTEMPTS - user_obj.unsuccessful_login_attempts} attempts remaining."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token = Token.objects.get_or_create(user=user_obj)
        
        ## Clearing Login attempt data:
        user_obj.blocked_until = None
        user_obj.unsuccessful_login_attempts = 0
        user_obj.save()

        FileIO.write_token_to_file(user_obj.username, token)
        
        logger.info(f"OTP validated for user: {user_obj.username}")
        logger.info(f"{user_obj.username} has sucessfully logged in.")

        ## Deleting the consumed OTP.
        user_otp.delete()

        return Response(
                    {
                        "status": True,
                        'user_id': user_obj.id, 
                        'username': user_obj.username,
                        'first_name': user_obj.first_name, 
                        'last_name': user_obj.last_name, 
                        'email': user_obj.email,
                        "token": str(token[0]),
                    },
                    status=status.HTTP_202_ACCEPTED,
                    headers=self.headers,
                    content_type="application/json"
                )
