from rest_framework.serializers import ModelSerializer
from .models import Article,Annotation,Comment
from rest_framework import serializers

#  https://stackoverflow.com/questions/17280007/retrieving-a-foreign-key-value-with-django-rest-framework-serializers

class ArticleSerializer(ModelSerializer):
    annotations = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Article
        read_only_fields = ('id','annotations')
        fields = ('id','link','annotations')

class AnnotationSerializer(ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Annotation
        read_only_fields = ('id','article','comments')
        fields = ('id','article','start_index','end_index','created_at','comments')

class CommentSerializer(ModelSerializer):
    annotation = serializers.StringRelatedField(source='annotation',read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
