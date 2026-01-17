from django.db import models

# Create your models here.
class UserProfile(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=250, null=True, blank=True)
    MobileNumber = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)   
    Status = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False              # 🔥 VERY IMPORTANT
        db_table = 'app_Users'       # exact table name