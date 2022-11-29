from django.urls import path
from polls.content.views import UploadFeed, Profile, UploadReply, ToggleLike, ToggleBookMark

urlpatterns = [
    path('upload',UploadFeed.as_view()),
    path('profile',Profile.as_view()),
    path('reply',UploadReply.as_view()),
    path('like',ToggleLike.as_view()),
    path('bookmark',ToggleBookMark.as_view())
]
