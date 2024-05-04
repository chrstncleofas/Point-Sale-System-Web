from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    UserID = models.CharField(max_length=10, unique=True, blank=True)
    Age = models.CharField(max_length=500, default='')
    Gender = models.CharField(max_length=500, default='')
    Address = models.CharField(max_length=500, default='')
    Position = models.CharField(max_length=500, default='')
    def save(self, *args, **kwargs):
        if not self.pk:
            latest_user = CustomUser.objects.order_by('-id').first()
            if latest_user:
                latest_user_id = int(latest_user.UserID[4:])
                self.UserID = f'USER{latest_user_id + 1:04}'
            else:
                self.UserID = 'USER0001'
        super().save(*args, **kwargs)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class TableStocks(models.Model):
    ProductID = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    Category = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Qty = models.CharField(max_length=500)
    BuyingPrice = models.CharField(max_length=500)
    SellingPrice = models.CharField(max_length=500)

class TableInventory(models.Model):
    ProductID = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    Category = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Qty = models.CharField(max_length=500)
    BuyingPrice = models.CharField(max_length=500)
    SellingPrice = models.CharField(max_length=500)
    Image = models.ImageField(upload_to='product_images/')

class TableTransaction(models.Model):
    TransactionID = models.CharField(max_length=500)
    ProductID = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Qty = models.CharField(max_length=500)
    UnitPrice = models.CharField(max_length=500)
    TotalAmount = models.CharField(max_length=500)
    DateTime = models.CharField(max_length=500)
    CashierName = models.CharField(max_length=500)

class TableTemp(models.Model):
    ProductID = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Qty = models.CharField(max_length=500)
    UnitPrice = models.CharField(max_length=500)
    TotalAmount = models.CharField(max_length=500)
