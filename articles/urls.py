from django.urls import path, include
from articles import views

# app_name='articles' 을 지정해주면 articles 를 장고템플릿에서 식별 할 수 있다.
app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    # url 자체를 변수처럼 동적으로 사용할 수 있는것이 변수url이다.
    path('dinner/', views.dinner, name='dinner'),
    # name="" 을 지정해주면 articles/review/에 대한 값을 받을 수 있다.
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
