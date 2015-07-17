from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    """(Category description)"""
    name = models.CharField(_('name'), blank=True, max_length=100)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        app_label = 'events'
        
class Event(models.Model):
    """(Event description)"""
    owner = models.ForeignKey(User, related_name='owner')
    title = models.CharField(_('title'), blank=True, max_length=100)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    location = models.CharField(_('location'), blank=True, max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    categories = models.ManyToManyField(Category)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Event"

    class Meta:
        app_label = 'events'