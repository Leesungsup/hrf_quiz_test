from rest_framework import serializers
from .models import Quiz,Player_info
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=('title','body','answer')
class PlayerSerializer(serializers.ModelSerialize):
    class Meta:
        model=Player_info
        fields=('number','name','position','age','nation','team','value')
