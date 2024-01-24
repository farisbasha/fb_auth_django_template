from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

from apps.drf_registration.models import CustomUser



@receiver(pre_save,sender = CustomUser)
def create_custom_user(sender, instance, **kwargs):
    if instance.id is None:
        emailName = instance.email.split('@')[0]
        if len(emailName) > 15:
            emailName = emailName[:15]
        kusername = slugify(emailName)
        counter = 1
        while CustomUser.objects.filter(username=kusername):
            kusername = kusername + str(counter)
            counter += 1
        instance.username = kusername
        
        if instance.role != CustomUser.USER_ROLES.ADMIN:
            instance.is_staff = False
            instance.is_superuser = False