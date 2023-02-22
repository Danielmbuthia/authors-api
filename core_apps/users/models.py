import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    first_name = models.CharField(max_length=80, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=80, verbose_name=_('last_name'))
    username = models.CharField(max_length=255,unique=True,db_index=True)
    email = models.EmailField(max_length=255,verbose_name=_('email'),db_index=True,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = UserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def __str__(self) -> str:
        return self.username
    
    @property
    def get_full_name(self):
        first_name = self.first_name.title()
        last_name = self.last_name.title()
        return first_name + ' ' + last_name
    
    
    
