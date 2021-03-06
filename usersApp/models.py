from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

  def create_user(self, username, password = None):

    if not username:
      raise ValueError('Users must have an username')

    user = self.model(username = username)
    user.set_password(password)
    user.save(using = self._db)

    return user


  def create_superuser(self, username, password):

    user = self.create_user(username = username, password = password)
    user.is_superuser = True
    user.save(using = self._db)

    return user

class BankUser(AbstractBaseUser, PermissionsMixin):
  
  id = models.BigAutoField(primary_key=True)
  username = models.CharField('Name', max_length = 15, unique=True) 
  password = models.CharField('Password', max_length = 256) 
  objects = UserManager()

  USERNAME_FIELD = 'username'


