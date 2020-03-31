from django.conf.urls import url
from django.urls import path
from . import views, views_data
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('auth/', obtain_auth_token, name='auth'),
    path('user/', views.UserManage.as_view(), name='user'),
    path('upload/', views.FileUpload.as_view(), name='upload'),
    path('work/', views_data.WorkView.as_view(), name='work'),
    path('work/<int:pk>/', views_data.WorkDetail.as_view()),
    path('page/', views_data.PageView.as_view(), name='page'),
    path('page/<int:pk>/', views_data.PageDetail.as_view()),
    path('word/', views_data.WordView.as_view(), name='word'),
    path('word/<int:pk>/', views_data.WordView.as_view()),
    path('radical/', views_data.RadicalView.as_view(), name='radical'),
    path('radical/<int:pk>/', views_data.RadicalView.as_view()),
    path('user-record/', views.UserRecordView.as_view(), name='user-record'),
]
