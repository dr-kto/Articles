from django.urls import path
# from django.urls.resolvers import URLPattern

from django.contrib.auth import views

from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]