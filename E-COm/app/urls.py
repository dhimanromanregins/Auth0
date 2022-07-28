from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')),
    path('profile/', views.profile),
    path('blog/',views.Blog),
    path('single_blog/<str:pk>',views.single_blog),
    path('', include('django.contrib.auth.urls')),
]