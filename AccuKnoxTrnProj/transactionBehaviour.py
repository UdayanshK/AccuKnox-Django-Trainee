import os
import django

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AccuKnoxTrnProj.settings')

# Initialize Django
django.setup()

# Now you can import models and run your code
from myapp.models import MyModel
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import transaction
from myapp.models import MyModel

# Make a signal that gets sent out when MyModel gets saved
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal received for {instance.name}")

def signal_test():
    try:
        # begin a db transaction, changes comiit only when transaction ends
        with transaction.atomic():
            # Create and save an object inside the transaction
            obj = MyModel.objects.create(name="Test Object")
            print("Object created in the transaction")
            # Raise an exception so the transaction gets rolled back
            raise Exception("Rolling back the transaction")
    except Exception as e:
        print(f"Transactiom rolled back: {e}")

    # Check if the signal handler still ran
    print("End of test")

# Calling the test function
signal_test()

#Answer: DJANGO SIGNALS DO NOT RUN IN THE SAME DB TRANSACTION AS THE CALLER, UNLESS EXPLICITLY CONFIGURED TO DO SO

# The signal is fired before the transaction is committed,
# meaning the signal handler is called when the model's save() method is executed,
# not when the transaction is committed.
# So, even if the transaction is rolled back later, the signal still runs.
# The signal handler runs even though the transaction is rolled back
# (and the object is not actually saved to the database).
# This indicates that the signal is not bound to the success or failure of the transaction.
# Instead, it is triggered as soon as the database save operation is attempted,
# regardless of the eventual outcome of the transaction.