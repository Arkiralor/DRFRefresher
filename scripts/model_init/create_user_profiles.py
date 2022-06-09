"""
Script to link all previously existing users to their respective profiles.

0. ./manage.py shell
1. from scripts.create_user_profiles import add_profile
2. add_profile()
"""

from userapp.models import User, UserProfile
from scripts import logger


def add_profile():
    """
    Creates user profiles for users that don't have one.

    This mainly deals with users in system who existed before the profile model was incorporated.
    """
    user_list = User.objects.all()
    logger.info("Retrieving all users...")

    for user in user_list:
        logger.info(f"Checking profile for User: {user.username}.")
        profile = UserProfile.objects.filter(user=user).first()
        if not profile:
            logger.info(f"No profile found for User: {user.username}.")
            profile = UserProfile.objects.create(user=user)
            logger.info(
                f"Creating Profile: {profile} for User: {user.username}.")
            profile.save()

        logger.info(f"Profile: {profile.id} for User: {user.username}.")


if __name__ == "__main__":
    add_profile()
