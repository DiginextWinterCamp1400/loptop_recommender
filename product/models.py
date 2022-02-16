from email.contentmanager import raw_data_manager
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
        company = models.CharField(max_length=200)
        product_name = models.CharField(max_length=200)
        type_name = models.CharField(max_length=200) 
        inches = models.FloatField()
        screen_resoulation = models.CharField(max_length=200)
        cpu = models.CharField(max_length=200)
        ram = models.CharField(max_length=200)
        memory = models.CharField(max_length=200) 
        gpu = models.CharField(max_length=200)
        opsys = models.CharField(max_length=200)
        weight = models.CharField(max_length=200)
        price = models.FloatField()
        created = models.DateTimeField(auto_now_add=True ,null=True)
        updated = models.DateTimeField(auto_now=True, null=True)
        slug = models.SlugField(max_length=200, unique=True, null=True)

        class Meta:
            ordering = ('product_name',)

        def __str__(self):
            return self.product_name
            
        def save(self, *args, **kwargs):
            self.slug = slugify(self.product_name, allow_unicode=True)
            super(Product, self).save(*args, **kwargs)