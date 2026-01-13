from django.db import models



class AppUsers(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=250, null=True, blank=True)
    MobileNumber = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50)
    SaltPassword = models.CharField(max_length=50)
    Status = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False              # 🔥 VERY IMPORTANT
        db_table = 'app_Users'       # exact table name