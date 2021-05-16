from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article,Annotation,Comment
from .serializers import ArticleSerializer,AnnotationSerializer,CommentSerializer

# Create your views here.
class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class AnnotationViewSet(ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
