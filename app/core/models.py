from django.db import models

from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# Create your models here.

class StudentManager(BaseUserManager):

    def create_user(self,enrollment,password=None,**extra_field):
        user=self.model(enrollment=enrollment,**extra_field)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self,enrollment,password):
        user=self.create_user(enrollment,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Student(AbstractBaseUser,PermissionsMixin):

    enrollment=models.CharField(max_length=100,unique=True)
    #email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    #classid=models.CharField(max_length=100)
    #degreeid=models.CharField(max_length=100)
    #enrollmentYear=models.IntegerField()
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects=StudentManager()

    USERNAME_FIELD= 'enrollment'

