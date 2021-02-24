from django.db import models

# Create your models here.


class Costumers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return 'Name: %s, Adress: %s, Mail: %s, Phone: %s' % (self.name, self.address, self.mail, self.phone)


class Article(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return 'Article: %s, Section: %s, Price: %s' % (self.name, self.section, self.price)


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    received = models.BooleanField()