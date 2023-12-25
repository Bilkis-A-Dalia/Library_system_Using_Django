from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.username}-{self.book.title}'