from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # rating = models.ManyToManyField(User,related_name='posts')
    image = models.ImageField(upload_to="book_img/")
    def __str__(self):
        return self.name


RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class BookReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    # review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.review_rating

# Create your models here.
