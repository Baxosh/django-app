from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.news_create, name='news_create'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('<int:pk>/update/', views.news_update, name='news_update'),
    path('<int:pk>/delete/', views.news_delete, name='news_delete'),
    # path('<int:pk>/comment/', views.comment, name='news_delete'),
]
