from django.db import models

#here after making first time schema if we ad new fiels in table then we have to put value for previous added entry what it them value in the this new field
#so for that we use default
#so this default is set to all previous recored present in the table
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_category = models.CharField(max_length=50,default="")
    product_subcategory = models.CharField(max_length=50,default="")
    product_description = models.CharField(max_length=500)
    product_public_date = models.DateField()
    product_image = models.ImageField(upload_to="shop/images",default="")

    #to show product name in admin panel not a product object(1) and etc ...
    #for these method no need to migration command run only save and after reload show it in admin pannel
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=10,default="")
    description = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name
