from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

app_name = "news"
urlpatterns = [
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>/", views.NewsDetail.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("category/<str:pk>/", views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
