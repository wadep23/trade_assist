from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="app")
    edited_at = models.DateField(null=True)
    edited_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="accounts"
    )
    account_type = models.CharField(max_length=100, default="Basic")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="app")
    edited_at = models.DateTimeField(null=True)
    edited_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.user.username}'s {self.get_account_type_display()} account"


class FinancialAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ("crypto", "Crypto"),
        ("stock", "Stock"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="financial_accounts",
    )
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    name = models.CharField(max_length=100, default="My Account")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="app")
    edited_at = models.DateField(null=True)
    edite_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.user.username}'s {self.get_account_type_display()} account"


class Asset(models.Model):
    symbol = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="app")
    edited_at = models.DateField(null=True)
    edited_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class Holding(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="holdings"
    )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    ammount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="app")
    edited_at = models.DateField(null=True)
    edited_by = models.CharField(max_length=100, null=True)

    class Meta:
        unique_together = ("account", "asset")

    def __str__(self):
        return (
            f"{self.account.user.username} holds {self.ammount} of {self.asset.symbol}"
        )
