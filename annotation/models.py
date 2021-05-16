from django.db import models
from accounts.models import UserAccount
# Create your models here.
class Article(models.Model):
    link = models.URLField(max_length=255)
    title = models.CharField(max_length =200)
    author = models.CharField(max_length = 200)
    def __str__(self):
        return str(self.link)

# class Annotation(models.Model):
#     article = models.ForeignKey(Line,on_delete=models.CASCADE,related_name='annotations')
#     start_index = models.IntegerField()
#     end_index = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.created_at)
class Line(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE)
    total_upvotes  = models.IntegerField(default = 0)
    total_downvotes = models.IntegerField(default = 0)
    total_agree= models.IntegerField(default = 0)
    total_disagree = models.IntegerField(default = 0)
    text  = models.CharField(max_length =100)
    def __str__(self):
        return str(self.text)

class Comment(models.Model):
    user = models.ForeignKey(UserAccount,on_delete = models.CASCADE)
    line = models.ForeignKey(Line,on_delete=models.CASCADE,related_name='comments')
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
    references = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    opinion = models.CharField(max_length = 1024)
    name = models.CharField(max_length  = 100,default = "John")
    agree = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.references) + " " +str(self.created_at) 

# class User(models.Model):
#     name = models.CharField(max_length = 100)
#     email = models.CharField(max_length = 100)
#     password = models.CharField(max_length =100)
#     def __str__(self):
#         return str({self.name} + " " +{self.email})

# # article
# # for lines in article.get_lines
# #     # pie chart line.total_upvotes and total_downvotes
# #     for comment in line.get_comments# to show top 5 comments 

# # server->object->template-rendering->




