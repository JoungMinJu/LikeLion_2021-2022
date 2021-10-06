#시리얼라이저
#Django의 model 데이터를 JSON 타입으로 변환(직렬화)
#JSON 타입으로 변환해야 API로 통신 가능!

from rest_framework import serializers

from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=('title','body','answer')

        