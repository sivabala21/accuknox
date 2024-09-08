from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('synchronous/', views.test_synchronous,name='synchronous'),
    path('thread/', views.test_thread,name='thread'),
    path('transaction/', views.test_transaction,name='transaction'),
]