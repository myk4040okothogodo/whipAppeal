from django.db import models
from django.conf import settings
# Create your models here.
import moneyed
from djmoney.models.fields import MoneyField


class Account(models.Model):
  owner = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  renewal_date = models.DateTimeField(null=False)

  account_balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
  def is_active(self):
    if  (timezone.now - renewal_date) < 30:
      return True     
  def is_premium(self):
    curr = account_balance
    curr = int(curr[1:])
    if curr < 20:
      return False
    return True  
  
