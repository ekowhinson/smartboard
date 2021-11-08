from django.db import models

# Create your models here.
class MenuGroup(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    ENABLE='1'
    DISABLE='0'
    STATUS=(
        (DISABLE,'Disable'),
        (ENABLE,'Enable'),
    )
    status=models.CharField(max_length=20,choices=STATUS,default=ENABLE)
    date=models.DateTimeField(auto_created=True,auto_now=True)
