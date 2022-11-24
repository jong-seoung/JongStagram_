from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# 같은 파일안에 .models라는 파일안에 Feed를 가지고옴
from .models import Feed
import os
from uuid import uuid4 # 랜덤한 아이디를 넣어줌
from config.settings import MEDIA_ROOT

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id') #select * from content_feed;
        return render(request,"jongstagram/main.html",context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self,request):

        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일을 읽어서 파일을 만들기
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        # 피드에 저장
        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image,like_count =0)


        return Response(status=200)