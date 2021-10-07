from typing import Tuple

from django.db import models
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    OPEN: str = 'open'
    CLOSED: str = 'closed'
    STATES: Tuple = (
        (OPEN, _('open')), (CLOSED, _('closed')),
    )

    name = models.CharField(
        verbose_name=_('restaurant_name'), help_text=_('restaurant_name'),
        max_length=128,
    )
    state = models.CharField(
        verbose_name=_('state'), help_text=_('state'),
        choices=STATES, default=CLOSED, max_length=10,
    )
    address = models.CharField(
        verbose_name=_('restaurant_address'),
        help_text=_('restaurant_address'), max_length=128,
    )
    rating = models.IntegerField(
        verbose_name=_('rating'), help_text=_('rating'),
        default=0,
    )
    phone = models.CharField(
        verbose_name=_('phone'), help_text=_('phone'),
        max_length=128,
    )
    cuisine = models.CharField(
        verbose_name=_('cuisine'), help_text=_('cuisine'),
        max_length=128,
    )
    is_active = models.BooleanField(
        verbose_name=_('is_active'), help_text=_('is_active'),
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('created'),
        verbose_name=_('created'),
    )
    modified = models.DateTimeField(
        auto_now=True, help_text=_('modified'),
        verbose_name=_('modified'),
    )

    class Meta:
        app_label = 'restaurant'
        db_table = 'restaurant.restaurants'
        verbose_name = _('restaurant')
        verbose_name_plural = _('restaurants')
