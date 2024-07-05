# from django.db import models

# # Create your models here.

# class Stu(models.Model):
#     name = models.CharField(max_length=200)
#     roll = models.IntegerField()
#     city = models.CharField(max_length=100)


# models.py

# models.py
# models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, phone_no, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, phone_no=phone_no, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, phone_no, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, first_name, last_name, phone_no, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, primary_key=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     phone_no = models.CharField(max_length=15, unique=True, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',
#         blank=True,
#         help_text=('The groups this user belongs to. A user will get all permissions '
#                    'granted to each of their groups.'),
#         verbose_name=('groups'),
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#         verbose_name=('user permissions'),
#     )

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_no']
    
#     def get_id(self):
#         return self.email  # Return a unique identifier for the user

#     def __str__(self):
#         return self.email


from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    def __str__(self):
        return self.title
    