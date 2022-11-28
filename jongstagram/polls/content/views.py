from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# 같은 파일안에 .models라는 파일안에 Feed를 가지고옴
from .models import Feed, Reply, Like, Bookmark
import os
from uuid import uuid4 # 랜덤한 아이디를 넣어줌
from config.settings import MEDIA_ROOT
from polls.user.models import User

class Main(APIView):
    def get(self,request):

        feed_object_list = Feed.objects.all().order_by('-id') #select * from content_feed;
        feed_list=[]

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []

            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(feed_id=reply.feed_id,
                reply_content=reply.reply_content,
                nickname = user.nickname))
                
            feed_list.append(dict(id = feed.id,
                image=feed.image,
                content=feed.content,
                like_count=feed.like_count,
                profile_image=user.profile_img,
                nickname=user.nickname,
                reply_list = reply_list
                ))
        email = request.session.get('email',None)

        if email is None:
            return render(request,"user/login.html")
        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request,"user/login.html")
        return render(request,"jongstagram/main.html",context=dict(feed_list=feed_list, user=user))

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
        email = request.session.get('email',None)

        # 피드에 저장
        Feed.objects.create(image=image, content=content,email=email, like_count =0)


        return Response(status=200)
    
class Profile(APIView):
    def get(self,request):
        email = request.session.get('email',None)

        if email is None:
            return render(request,"user/login.html")
        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request,"user/login.html")        
        return render(request,'content/profile.html',context=dict(user=user))
    
class UploadReply(APIView):
    def post(self,request):
        feed_id = request.data.get('feed_id',None)
        reply_content = request.data.get('reply_content',None)
        email = request.session.get('email',None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content,email=email)

        return Response(status=200)
    