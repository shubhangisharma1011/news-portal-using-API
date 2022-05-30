from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

#User Model Login with email + use for login registration (Default Model)
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.utils.translation import ugettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Profile(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    file = models.FileField(upload_to="Update_Profile", default='images.png')

class CustomUser(AbstractUser):
    """User model."""
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True, null=True, blank=True)
    file = models.FileField(upload_to="User_Images", default='images.png')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


#a new models for email verification by link
class User_Model_Email_Verification(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    token = models.CharField(max_length=150)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.token

"""
class Blog(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True,null=True)
    #content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['user_id']

    def __str__(self):"""
#        return self.title