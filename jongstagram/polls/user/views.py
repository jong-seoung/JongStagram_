from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
from uuid import uuid4 # 랜덤한 아이디를 넣어줌
from config.settings import MEDIA_ROOT
import os
# 회원 가입 창
class Join(APIView):
    def get(self,request):
        return render(request,"user/join.html")
    
    def post(self,request):
        # 회원 가입
        email=request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,nickname=nickname,name=name,password=make_password(password),profile_img = "default_profile.jpg")
    
        return Response(status=200)
        
# 로그인 창
class login(APIView):
    def get(self,request):
        return render(request,"user/login.html")

    def post(self,request):
        email=request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))
        
        if user.check_password(password):
            # 로그인을 했다. 세션 or 쿠키에 넣는다
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data= dict(message="회원정보가 잘못되었습니다."))

# 로그 아웃
class logout(APIView):
    def get(self,request):
        request.session.flush()
        return render(request,"user/login.html")
    

class Uploadprofile(APIView):
    def post(self,request):

        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일을 읽어서 파일을 만들기
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name
        email = request.data.get('email')

        user = User.objects.filter(email=email).first()

        user.profile_img = profile_image
        user.save()


        return Response(status=200)
    