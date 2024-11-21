from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.db import models
from shortuuidfield import ShortUUIDField

class IEUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        创建用户
        """
        if not username:
            raise ValueError("必须设置真实姓名!")
        user = self.model(username=username, **extra_fields)
        # email = self.normalize_email(email)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        创建普通用户
        """
        # extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """
        创建超级用户
        """
        # extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("超级用户必须设置is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("超级用户必须设置is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

class IEUser(AbstractBaseUser, PermissionsMixin):
    """
    重写的用户类
    """
    uid = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=30 , blank=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = IEUserManager()

    USERNAME_FIELD = "username"    # 这是用来鉴权的, 他会把值作为指定字段来做验证
    REQUIRED_FIELDS = ['password'] # 指定哪些字段必要, 其他FIELD中的除外


    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username