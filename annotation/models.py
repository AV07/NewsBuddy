from django.db import models

# Create your models here.
class Article(models.Model):
    link = models.URLField(max_length=255)

    def __str__(self):
        return str(self.link)

class Annotation(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='annotations')
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)

class Comment(models.Model):
    annotation = models.ForeignKey(Annotation,on_delete=models.CASCADE,related_name='comments')
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    references = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.references) + " " +str(self.created_at) 
