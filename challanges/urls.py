from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # /challanges/ path
    # placeholder, handle all urls with text after challanger
    path('<int:month>', views.monthly_challange_by_number),
    path('<str:month>', views.monthly_challange, name='month_challange'),
]
