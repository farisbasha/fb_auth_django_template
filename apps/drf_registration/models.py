from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _






class CustomUser(AbstractUser):
    class USER_ROLES(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        STAFF = 'staff', _('Staff')
        STUDENT = 'student', _('student')
    
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=20, choices=USER_ROLES.choices,default=USER_ROLES.STUDENT)
    image = models.ImageField(upload_to='profile_pics',default='user.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','role']

    def __str__(self):
        return self.email
    class Meta:
        ordering = ['-date_joined']
        
        


