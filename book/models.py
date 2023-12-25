from django.db import models
from category.models import Category

# Create your models here.

class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book/media/uploads')
    title = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Comment by {self.name}'