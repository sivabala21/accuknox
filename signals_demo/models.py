from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class SynchronousModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SynchronousModel)
def synchronous_signal_handler(sender, instance, **kwargs):
    print(f"Synchronous signal received for: {instance.name}")

class ThreadModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=ThreadModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    print(f"Signal handler thread ID: {threading.get_ident()}")
    time.sleep(2)  # Simulate delay
    print("Signal handler finished")

class TransactionModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TransactionModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    instance.name = "Modified"
    instance.save()