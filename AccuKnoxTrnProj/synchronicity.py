import time
from django.dispatch import Signal, receiver

# making a custom signal
mySignal = Signal()

@receiver(mySignal)
def myReceiver(sender, **kwargs):
    print("received the signal, will take 5 sec to simulate a process...");
    time.sleep(5)
    print("process completed!")

def mySender():
    print("sending signal to receiver...")
    mySignal.send(sender=None)
    print("signal sent. reciever has told me that it has completed its work.")

# now we send the signal
# if the signal execution were asynchronous,
# the line "signal sent. recei..." would be printed immediately,
# without waiting for the receiver to complete its task.
mySender()