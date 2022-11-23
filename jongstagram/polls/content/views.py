from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# 같은 파일안에 .models라는 파일안에 Feed를 가지고옴
from .models import Feed 

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id') #select * from content_feed;
        return render(request,"jongstagram/main.html",context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self,request):
        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        print(file)
        print(image)
        print(content)
        print(user_id)
        print(profile_image)


        return Response(status=200)