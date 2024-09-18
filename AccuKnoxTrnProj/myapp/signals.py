from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

# make a reciever for dummyapp
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal received for: {instance.name}")

    if created:
        print(f"New object created: {instance.name}")
    else:
        print(f"Existing object updated: {instance.name}")