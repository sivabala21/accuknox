# Accuknox Django Trainee Assignment

### Question 1: By default, are Django signals executed synchronously or asynchronously?

**Answer:**  
Yes, by default, Django signals are executed synchronously, which means they are executed one after the other.

To demonstrate this, we define a model and a trigger function to show the synchronous execution of signals.

### demonstration:

```python
# signals_demo/models.py

# Defining model to show signals execution in a synchronous manner.

class SynchronousModel(models.Model):
    name = models.CharField(max_length=100)

# Signal function to show the synchronous execution of signals.
@receiver(post_save, sender=SynchronousModel)
def synchronous_signal_handler(sender, instance, **kwargs):
    print(f"Synchronous signal received for: {instance.name}")

# signals_demo/views.py

# A Trigger function to create an object so that we can see the signals' execution in a synchronous manner.
def test_synchronous(request):
    obj = SynchronousModel.objects.create(name="Test Synchronous")
    return HttpResponse("Synchronous test completed, check console")

```

This shows the signals execution one after the other in synchronous manner by default.

#### Question 2: Do Django signals run in the same thread as the caller?

**Answer:**

Yes, Django signals are run in the same thread as the caller.

### demonstration:

```python
# signals_demo/models.py

# Defining model to show signals run in the same thread as the caller.
class ThreadModel(models.Model):
    name = models.CharField(max_length=100)

# Signal function to show the same thread execution as the caller.
@receiver(post_save, sender=ThreadModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    print(f"Signal handler thread ID: {threading.get_ident()}")
    time.sleep(2)  # Simulate delay
    print("Signal handler finished")

# signals_demo/views.py

# A Trigger function to create an object so that we can see the signals' execution in the same thread as the caller.
def test_thread(request):
    obj = ThreadModel.objects.create(name="Test Thread")
    print(f"View thread ID: {threading.get_ident()}")
    return HttpResponse("Thread test completed check console")

```

This shows the signals execution in the same thread as the caller.

### Question 3: Question 3: By default, do Django signals run in the same database transaction as the caller?

**Answer:**

Yes, Django signals are run in the same database transaction as the caller.

### demonstration:

```python
# signals_demo/models.py
# Defining model to show signals run in the same database transaction as the caller.
class TransactionModel(models.Model):
    name = models.CharField(max_length=100)
# Signal function modifying the name of the object. when the object is created by Trigger function.
@receiver(post_save, sender=TransactionModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    instance.name = "Modified"
    instance.save()

# signals_demo/views.py

# A Trigger function to create an object so that we can see the signals' execution in the same database transaction as the caller.
def test_transaction(request):
    obj = TransactionModel.objects.create(name="Original")
    print(f"Name before save: {obj.name}")
    with transaction.atomic():
        obj.name = "Updated"
        obj.save()
    print(f"Name after save: {obj.name}")

    return HttpResponse("Transaction test completed check console")

```

This shows the signals execution in the same database transaction as the caller.

### All this operation of signal is implemented in signals_demo django app. you can clone it and run it.

> [!Complete] Please Contact me if my assignment is not clear [sivabala](mailto:sivabala.s@outlook.com)
