from django.db import models

# Create your models here.

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    BookingDATE = models.DateField()

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'