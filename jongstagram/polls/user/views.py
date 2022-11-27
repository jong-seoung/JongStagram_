from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password

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