import time
from django.dispatch import Signal, receiver

# making a custom signal
mySignal = Signal()

@receiver(mySignal)
def myReceiver(sender, **kwargs):
    print("myReceiver has received the signal, will take 5 sec to simulate a process...");
    time.sleep(5)
    print("myReceiver has completed its process!")

def mySender():
    print("mySender is sending signal to receiver...")
    mySignal.send(sender=None)
    print("mySender has sent the signal and myReceiver just told mySender that it has completed its process")

# let us send the signal
mySender()

# if the signal execution were asynchronous,then the line
# "mySender speaking..." would be printed immediately,
# without waiting for the receiver to complete its task.
# but alas, that did not happen,
# proving that signals are executed synchronously