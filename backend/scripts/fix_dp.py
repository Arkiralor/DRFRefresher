"""
Script to migrate user profile pictures to new default image.
"""

from userapp.models import UserProfile
from scripts import logger

def main():
    profiles = UserProfile.objects.all()
    logger.info(f"Retrieved {len(profiles)} profiles")
    for profile in profiles:
        logger.info(f"Updating profile {profile.user.username}")
        try:
            profile.profile_picture = "images/defaults/profile_picture.png"
            profile.save()
        except Exception as ex:
            logger.error(f"Error updating profile {profile.user.username}")
            logger.error(f"{ex}")

if __name__ == "__main__":
    main()
    