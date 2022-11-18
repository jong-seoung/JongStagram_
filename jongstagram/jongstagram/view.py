from django.shortcuts import render
from rest_framework.views import APIView


class main(APIView):
    def get(self,request):
        print("겟으로 호출")
        return render(request,"jongstagram/main.html")
    

    def post(self,request):
        print("포스트으로 호출")
        return render(request,"jongstagram/main.html")