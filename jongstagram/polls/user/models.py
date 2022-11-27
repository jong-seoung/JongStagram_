from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    """
     유저 프로필 파일
     유저 닉네임
     유저 이름 - 본명
     유저 이메일 주소
     유저 비밀번호 
    """

    profile_img = models.TextField()
    nickname = models.CharField(max_length=24,unique=True) # 24글자를 넘지않음
    name = models.CharField(max_length= 24)
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = 'User'
