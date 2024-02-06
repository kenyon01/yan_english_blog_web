from django.urls import path
from . import views

app_name = 'displaytext'

urlpatterns = [
    path('displaytext/', views.my_new_page, name='my_new_page'),
]
