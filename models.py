
from django.db import models
import datetime
class SubscriptionTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    subscription_code = models.CharField(max_length=50)
    subscription_description = models.CharField(max_length=500)
    subscription_web_description = models.CharField(max_length=500)
    subscription_mobile_description = models.CharField(max_length=500)
    subscription_image = models.CharField(max_length=150)
    subscription_is_default = models.BooleanField(default=False)
    subscription_is_demo = models.BooleanField(default=False)
    created_by_user_id = models.BigIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_from_ip = models.GenericIPAddressField(null=True, blank=True)
    updated_by_user_id = models.BigIntegerField(null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_from_ip = models.GenericIPAddressField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)


    class Meta:
        managed = True
        db_table = 'subscription_types'

