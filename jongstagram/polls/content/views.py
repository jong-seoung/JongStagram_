from django.shortcuts import render
from rest_framework.views import APIView
# 같은 파일안에 .models라는 파일안에 Feed를 가지고옴
from .models import Feed 

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id') #select * from content_feed;
        return render(request,"jongstagram/main.html",context=dict(feed_list=feed_list))
    