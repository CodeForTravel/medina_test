from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(
        verbose_name=_("email address"), unique=True,
        error_messages={
            'unique': _(
                "A user is already registered with this email address"),
        },
    )

    class UserTypes(models.IntegerChoices):
        ADMIN = 1, _("Admin")
        CONSUMER = 2, _("Consumer")
        VENDOR = 3, _("Vendor")
        
        

    user_type = models.IntegerField(
        _("User Type"), choices=UserTypes.choices, null=True, blank=True, default=UserTypes.ADMIN
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    """Use the email as unique username."""

    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


    @property
    def is_admin(self):
        if self.user_type == self.UserTypes.ADMIN:
            return True
        return False

    @property
    def is_consumer(self):
        if self.user_type == self.UserTypes.CONSUMER:
            return True
        return False

    @property
    def is_vendor(self):
        if self.user_type == self.UserTypes.VENDOR:
            return True
        return False