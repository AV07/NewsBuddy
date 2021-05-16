from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from accounts.models import UserAccount
# from .serializers import ArticleSerializer,AnnotationSerializer,CommentSerializer
from django.http import HttpResponse
import trafilatura
from django.http import JsonResponse
# Create your views here.
# class ArticleViewSet(ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

# class AnnotationViewSet(ModelViewSet):
#     serializer_class = AnnotationSerializer
#     queryset = Annotation.objects.all()

# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()

def home(request):
    return render(request,'homepage.html')

def profile(request):
    return render(request,'userprofile.html',context  = {'user':request.user})

def add_annotation(request):
    print(request.POST)
    line_id = request.POST['id']
    text = request.POST['text']
    link1 = request.POST['link']
    # link2 = request.POST['link2']
    agree  = request.POST['agree']
    agree = str.lower(agree)
    print(agree)
    line = Line.objects.get(id = line_id)
    if agree == 'yes':
        line.total_upvotes += 1
    else:
        line.total_downvotes += 1
    comment = Comment(user = request.user ,line =  line, references = str(link1) ,opinion = text,agree = agree == "yes")
    comment.save()
    line.save()
    return render(request,'index.html',context = {'article':line.article})

def vote(request):
    comment_id = request.POST['id']
    vote_amt = int(request.POST['vote'])
    comment = Comment.objects.get(id= comment_id)
    line = comment.line
    if vote_amt > 0:
        comment.upvotes +=1
        line.total_upvotes+=1
    else:
        comment.downvotes -=1
        line.total_downvotes -=1
    line.save()
    comment.save()
    return JsonResponse({'done':True})

    # comment.article.total_upvotes+=1
def get_article(request):
    url = request.POST.get('url',None)
    if url is not None and url!='':
        try:
            article  = Article.objects.get(link = url)
        except Article.DoesNotExist as e:
            downloaded = trafilatura.fetch_url(url)
            text = trafilatura.bare_extraction(downloaded,include_images = True,include_links=True,include_formatting = True)
            article = Article(link = url,author = text['author'] if text['author'] is not None else "Author",title = text['title'] if text['title'] is not None else "Title")
            article.save()
            for line in text['text'].split('.'):
                Line(text = line, article = article).save()
        # return HttpResponse(f"{article}")
        return render(request,'index.html',context = {'article':article})