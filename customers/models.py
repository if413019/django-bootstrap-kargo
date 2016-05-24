from __future__ import unicode_literals

import uuid as uuid

from django.db import models

# every Django model fields can be customized by re-use parameter under
# simple dictionary format 

class CommonInfo(models.Model):
    """
    Abstract models contains mandatory fields on each models.
    Every class can have these fields by instantiate from this class.
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name='Waktu Dibuat')
    modified = models.DateTimeField(auto_now=True, verbose_name='Waktu diedit')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    # flag for update, delete, sync and coming from cloud
    is_delete = models.BooleanField(default=False, verbose_name='Soft Delete')

    class Meta:
        abstract = True


class ODCustomer(CommonInfo):
    """
    Order details contain name, phone and amount of total price order 
    """
    name = models.CharField(max_length=30)
    email = models.EmailField(blank = False)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=128)
    picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')



    def __unicode__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Customers"
