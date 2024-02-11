from django.db import models
from django.forms import ModelForm
from webapp.models import enter,Product
# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(enter,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField() 
    amount = models.IntegerField()
class cartForm(ModelForm):
    class Meta:
        model = cart
        fields = ["user","product","qty","price","amount"]