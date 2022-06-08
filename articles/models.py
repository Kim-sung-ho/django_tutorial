from django.db import models

# Create your models here.
class Article(models.Model): #상속
    title = models.CharField(max_length=10)
    #aksg
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
