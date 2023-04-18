from unittest.util import _MAX_LENGTH
from django.db import models
from phone_field import PhoneField

# Create your models here.


class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

        
class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.TextField(max_length=255)
    dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'



class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=255)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors , on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class Contact(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    remark = models.TextField(255)