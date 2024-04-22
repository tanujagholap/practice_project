from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Create


@receiver(post_save, sender=Create)
def create_save(sender, instance, created, **kwargs):
    if created:
        print('new added')

    print(created)


@receiver(post_delete, sender=Create)
def create_save1(sender, instance, **kwargs):
    print(f'{instance.f_name} record deleted')