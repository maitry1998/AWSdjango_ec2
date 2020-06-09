from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf import views
from .views import ArticleListView,ArticleintView,GenericAPIView
urlpatterns = [
    # path('', ArticleListView.as_view()),
    path('generic/detail/<int:id>', GenericAPIView.as_view()),
    # path("help/", views.form_function),

]
