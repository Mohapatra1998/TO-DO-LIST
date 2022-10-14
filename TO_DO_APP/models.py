from django.db import models

# Create your models here.
class work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500,editable=False,unique=True)
    date = models.DateField()
    status_dict=(
        ('Active Task','Active Task'),
        ('Completed','Completed'),
        ('Upcoming','Upcoming'),
    )
    work_status=models.CharField(max_length=150, choices=status_dict)
    discription=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)