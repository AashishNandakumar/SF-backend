from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group,Permission

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=3)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=9)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-image-url')  # s3 object link to image
    document_url = models.CharField(max_length=500, default='/no-doc-url') # s3 object link to document

    def __str__(self):
        return self.name
class UserManager(BaseUserManager):
    def create_user(self,email=None,phone=None,password=None):
        if not email and not phone:
            raise ValueError('Users must enter either one')
        email=self.normalize_email(email)
        user=self.model(email=email,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email address'), unique=True, blank=True, null=True)
    phone = models.CharField(('phone number'), max_length=15, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set_custom",
        related_query_name="user_custom",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom",  # Changed related_name
        related_query_name="user_custom",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email if self.email else self.phone