# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    category = models.CharField(max_length=255, null=True, blank=True)
    category_code = models.IntegerField(null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Product(models.Model):

    #__Product_FIELDS__
    idcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.CharField(max_length=255, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    status = models.BooleanField()
    idbrand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Brand(models.Model):

    #__Brand_FIELDS__
    brand = models.CharField(max_length=255, null=True, blank=True)

    #__Brand_FIELDS__END

    class Meta:
        verbose_name        = _("Brand")
        verbose_name_plural = _("Brand")



#__MODELS__END
