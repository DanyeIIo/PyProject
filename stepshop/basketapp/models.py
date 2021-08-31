from django.db import models

from stepshop import settings

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )

    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=0
    )

    add_datetime = models.DateTimeField(
        verbose_name='time',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'basket'
        verbose_name_plural = 'basket'