from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .utils import generate_account_number

# Create your models here.

# Table


class Profile(models.Model):
    # columns
    """
    Class for the owner of the invoice
    """
    # Since it is one to one 1 user can have only one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # by setting blank to true we are making this field optional
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(default="images/avatar.png")
    company_logo = models.ImageField(default="images/no_photo.png")

    def __str__(self):
        return f"Profile of the use: {self.user.username}"

    # it overrides save method
    def save(self, *args, **kwargs):
        if self.account_number == '':
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

    # def clean(self):
    #     if len(self.account_number) != 26:
    #         raise ValidationError(
    #             'Bank account number must be 26 characters long')
