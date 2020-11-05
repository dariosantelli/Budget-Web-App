from django.db import models
from django.utils import timezone
import datetime
#MAKE SURE TO IMPORT TIMEZONE BEFORE DATETIME

budgetcategories = (('PERSONAL', 'Personal'), ('GROCERIES', 'Groceries'), ('HEALTH', 'Health'),)

class Main(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=200, choices=budgetcategories)