from django.db import models

category_choices = (
    ('shoes','shoes'),
    ('mobile_accessories','mobile_accessories'),
    ('caps','caps'),
    ('watches','watches'),
)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    d_price = models.IntegerField()
    brand = models.CharField(max_length=30)
    description = models.CharField(max_length=3000, default="")
    about_1 = models.CharField(max_length=300)
    about_2 = models.CharField(max_length=300)
    about_3 = models.CharField(max_length=300)
    category = models.CharField(choices=category_choices, max_length=20, default="")
    image = models.ImageField(upload_to = 'product_images')
    def __str__(self):
        return self.name

tracker_choice = (
    ('Your Order has been Recieved','Your Order has been Recieved'),
    ('Packed','Packed'),
    ('Ship','Ship'),
    ('In your City','In your City'),
    ('Recieved By You','Recieved By You')
)

class Order(models.Model):
    products_ordered = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    first_address = models.CharField(max_length=300)
    second_address = models.CharField(max_length=300)
    tracker = models.CharField(choices=tracker_choice, max_length=100, default="Your Order has been Recieved")

    def __str__(self):
        return self.products_ordered