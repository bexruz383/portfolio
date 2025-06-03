from django.urls import path

from app.views import index_wiev, contact_view

urlpatterns = [
    path('', index_wiev, name='index'),
    path('contact/', contact_view, name='contact'),
]