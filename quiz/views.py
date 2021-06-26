from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .models import Player_info
from .serializes import QuizSerializer
from .serializes import PlayerSerializer
import random
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")
@api_view(['GET'])
def hello(request):
    return Response("Hello!")
@api_view(['GET'])
def ket(request):
    return Response("KetAI")
@api_view(['GET'])
def op(request):
    return Response("opening")
@api_view(['GET'])
def randomQuiz(request,id):
    totalQuizs=Quiz.objects.all()
    randomQuizs=random.sample(list(totalQuizs),id)
    serializer=QuizSerializer(randomQuizs,many=True)#many=True 다수의 데이터 직렬화
    return Response(serializer.data)
@api_view(['GET'])
def player(request,pk):
    obj = Player_info.objects.get(number=pk)
    #totalPlayers=Player_info.objects.all()
    #randomPlayerQuizs=random.sample(list(totalPlayers),number)
    #serializer1=PlayerSerializer(randomPlayerQuizs,many=True)#many=True 다수의 데이터 직렬화
    serializer1=PlayerSerializer(obj)#many=True 다수의 데이터 직렬화
    return Response(serializer1.data)
@api_view(['GET'])
def playerQuiz(request,pk):
    totalPlayers=Player_info.objects.all()
    randomPlayerQuizs=random.sample(list(totalPlayers),pk)
    serializer2=PlayerSerializer(randomPlayerQuizs,many=True)#many=True 다수의 데이터 직렬화
    return Response(serializer2.data)