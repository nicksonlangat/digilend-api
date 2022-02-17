from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import CustomUserManager
CREDIT_STATUS = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Bad', 'Bad'),
    ('Defaulter', 'Defaulter')
]

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250, unique=True, null=True, blank=True)
    id_number = models.CharField(max_length=250, unique=True,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    front_id_image = models.ImageField(upload_to='front_id_images',null=True, blank=True)
    back_id_image = models.ImageField(upload_to='back_id_images',null=True, blank=True)
    is_kyc_approved = models.BooleanField(default=False)
    credit_status = models.CharField(choices=CREDIT_STATUS, default='Good', max_length=40)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
