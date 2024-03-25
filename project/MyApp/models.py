from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category

class Book(models.Model):

    ST = [
        ('Available','Available'),
        ('Rented','Rented'),
        ('Sold','Sold'),
    ]

    Title = models.CharField(max_length= 50)
    Auther_Name = models.CharField(max_length=50 , null=True , blank=True)
    Book_Photo = models.ImageField(upload_to="photes/Book_photes/%y/%m%d" , null=True , blank=True)
    Auther_Photo = models.ImageField(upload_to="photes/Auther_photes/%y/%m%d" , null=True , blank=True)
    Pages = models.IntegerField(null=True , blank=True)
    Price = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    States = models.CharField(max_length=50  , null=True , blank=True , choices=ST)
    category = models.ForeignKey(Category , on_delete=models.PROTECT , null=True , blank=True)

    def __str__(self) -> str:
        return self.Title
