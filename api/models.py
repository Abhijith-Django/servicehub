from django.db import models

# Create your models here.

from django.db.models import Sum

from django.contrib.auth.models import User

class Customer(models.Model):

    name=models.CharField(max_length=200)

    phone_number=models.CharField(max_length=200)

    email=models.CharField(max_length=200)

    vehicle_number=models.CharField(max_length=200)

    running_km=models.PositiveIntegerField()

    customer_status=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed")       
    )

    status=models.CharField(max_length=200,choices=customer_status,default="pending")

    technician=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    @property
    def work_count(self):

        return self.work_set.all().count

        # return Work.objects.filter(customer=self).count()
    
    @property
    def works(self):

        return self.work_set.all()
    
    @property
    def work_total(self):

        return self.work_set.all().values("amount").aggregate(total=Sum("amount"))["total"]

    def __str__(self):
        return self.name
    
 
    
class Work(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    amount=models.PositiveIntegerField()

    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
 