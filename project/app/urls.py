from django.urls import path
from .views import FileUploadView,chat_query

urlpatterns = [
        path('upload/', FileUploadView.as_view(), name='file-upload'),
        path('chat/', chat_query, name='chat-query'),

]
