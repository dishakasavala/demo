from django.db import models
from django.forms import ModelForm

# Create your models here.
class enter(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.BigIntegerField()
class enterForm(ModelForm):
    class Meta:
        model = enter
        fields = ["name","email","password","contact"]

class slider(models.Model):
    Title = models.CharField(max_length=100)
    Sub_title = models.CharField(max_length=100)
    image = models.FileField(upload_to="media/",default="")
class sliderForm(ModelForm):
    class Meta:
        model = slider
        fields = ["Title","Sub_title","image"]

class catagory(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="media/",default="")
class catForm(ModelForm):
    class Meta:
        model = catagory
        fields = ["name","image"]

class Category(models.Model):
    category = models.CharField(max_length=100)
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category"]

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    price = models.IntegerField()
    image = models.FileField(upload_to="media/",default="")
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title","category","price","image"]