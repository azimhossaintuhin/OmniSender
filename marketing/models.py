from django.db import models


class Setting(models.Model):
    token = models.CharField(max_length=50000, null=True ,blank=True)
    phone =  models.CharField(max_length=20 , null=True , blank=True)
    logger = models.BooleanField(default = True)
    update_check  = models.BooleanField(default = True)

    def __str__(self):
        return self.phone


class send_message(models.Model):
    phone = models.CharField( max_length=50)
    message =  models.TextField(null=True , blank=True)
    is_send = models.BooleanField(default=False)
    is_seen =  models.BooleanField(default=False) 
    created =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.phone







 