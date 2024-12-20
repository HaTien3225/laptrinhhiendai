
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

r = DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='cate')
r.register('courses', views.CourseViewSet, basename='course')
r.register('lesson', views.LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(r.urls))
]