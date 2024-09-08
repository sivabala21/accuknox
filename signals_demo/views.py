from django.http import HttpResponse
from django.db import transaction
from .models import SynchronousModel, ThreadModel, TransactionModel
import threading
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def test_synchronous(request):
    obj = SynchronousModel.objects.create(name="Test Synchronous")
    
    return HttpResponse("Synchronous test completed check console")

def test_thread(request):
    obj = ThreadModel.objects.create(name="Test Thread")
    print(f"View thread ID: {threading.get_ident()}")
    return HttpResponse("Thread test completed check console")

def test_transaction(request):
    obj = TransactionModel.objects.create(name="Original")
    print(f"Name before save: {obj.name}")
    with transaction.atomic():
        obj.name = "Updated"
        obj.save()
    print(f"Name after save: {obj.name}")

    return HttpResponse("Transaction test completed check console")
