from django.db import models
# The imports belows is what we use when customising the default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Permissions system
    is_active = models.BooleanField(default=True)
    # Used to determine if they have access to the Django Admin
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # Override the username field to use email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return String representation of user"""
        return self.email
