import threading
from django.dispatch import Signal, receiver

# make a signal for this demonstration
threadSignal = Signal()

# make a receiver
@receiver(threadSignal)
def threadReceiver(sender, **kwargs):
    print(f"signal received in thread: {threading.get_ident()}")

# and a sender
def threadSender():
    print(f"signal sent in thread: {threading.get_ident()}")
    threadSignal.send(sender="threadSender")

# now let's call the signal sender
threadSender()

# you should see 2 lines in the console
# that have the same thread id
# proving that a signal runs in the
# same thread as its caller