from django.db import models
from django.utils import timezone
# Create your models here.

class Restaurant(models.Model):
    # 이름, 전화번호, 주소, 작성일시
    name = models.CharField(max_length = 50) # 글자수 제한된 텍스트정의
    phone = models.CharField(max_length = 20)
    address = models.TextField() # 글자 수에 제한없는 긴 텍스트 위한 속성
    lat = models.FloatField(default = 0.0) # 실수
    lng = models.FloatField(default = 0.0) # 실수
    created = models.DateTimeField(default=timezone.now) #날짜와 시간간
