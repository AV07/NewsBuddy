from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet,AnnotationViewSet,CommentViewSet

router = DefaultRouter()
router.register("article",ArticleViewSet)
router.register("annotation",AnnotationViewSet)
router.register("comment",CommentViewSet)

urlpatterns = [
    path ("",include(router.urls))
]