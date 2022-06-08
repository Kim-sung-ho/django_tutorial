from django.db import models

# Create your models here.
class Article(models.Model): #상속
    #필드들을 저장하고, id는 자동으로 저장된다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
