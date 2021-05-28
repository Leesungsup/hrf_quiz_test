from django.urls import path, include
from .views import *
urlpatterns=[
    path("Hello/",helloAPI),
    path("<int:id>/",randomQuiz),
    path("Hello1/",hello),
    path("Ket/",KetAI),
]