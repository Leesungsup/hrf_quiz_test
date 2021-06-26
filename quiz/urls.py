from django.urls import path, include
from .views import *
urlpatterns=[
    path("Hello/",helloAPI),
    path("<int:id>/",randomQuiz),
    path("PlayerQuiz/<int:pk>/",playerQuiz),
    path("Player/<int:pk>/",player),
    path("Hello1/",hello),
    path("Ket/",ket),
    path("op/",op),
]