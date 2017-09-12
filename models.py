from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
    phone = models.CharField(max_length=20)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class UserInheritanceManager(UserManager): 
    def get_queryset(self): 
        return InheritanceQuerySet(self.model).select_subclasses()

    get_query_set = get_queryset 
