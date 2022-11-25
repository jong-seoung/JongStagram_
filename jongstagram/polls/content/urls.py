from django.urls import path
from polls.content.views import UploadFeed

urlpatterns = [
    path('upload',UploadFeed.as_view())
]
