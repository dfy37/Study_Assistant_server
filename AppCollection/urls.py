from django.urls import path
from AppCollection import collection

urlpatterns = [
    path('submit', collection.submit),
    path('sync', collection.sync),
    path('addentry', collection.addEntry),
    path('delentry', collection.delEntry),
]