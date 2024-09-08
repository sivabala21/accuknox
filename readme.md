# Accuknox Django Trainee Assignment

Question 1: By default, are Django signals executed synchronously or
asynchronously?

Answer : Yes By default django signals are executed synchronously which means they are executed one after the other

To demonstrate this
'''

# signals_demo\models.py

# Defining model to show signals execution in synchronous manner.

class SynchronousModel(models.Model):
name = models.CharField(max_length=100)

# signals_demo\views.py

# A Trigger function to create a object so that we can see the signals execution in synchronous manner.

def test_synchronous(request):
obj = SynchronousModel.objects.create(name="Test Synchronous")
return HttpResponse("Synchronous test completed check console")

# This Show the signals execution one after the other in synchronous manner by default.

'''
