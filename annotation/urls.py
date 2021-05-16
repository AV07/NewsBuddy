from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import ArticleViewSet,AnnotationViewSet,CommentViewSet
from . import views

app_name = 'annotation'
urlpatterns = [
    # path ("",include(router.urls)),
    path("article_view",views.get_article,name = 'article_view'),
    path("home",views.home,name = 'home'),
    path('add_annotation',views.add_annotation,name = 'add_annotation'),
    path('vote', views.vote, name='vote'),
    path('profile',views.profile, name = 'profile')
]
