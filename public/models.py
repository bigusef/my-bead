from django.db import models


class Mattress(models.Model):
    name = models.CharField('اﻷسم العربي', max_length=50)
    description = models.TextField('الوصف')
    features = models.TextField('المميزات')
    cover = models.ImageField('صوره المرتبه', upload_to='mattress')
    is_new = models.BooleanField('إظهار في الصفحه الرئيسيه', default=False)
    stampdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'المرتبه'
        verbose_name_plural = 'المراتب'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField('اﻷسم العربي', max_length=50)
    description = models.TextField('الوصف')
    features = models.TextField('المميزات')
    cover = models.ImageField('صوره المنتج', upload_to='product')
    is_new = models.BooleanField('إظهار في الصفحه الرئيسيه', default=False)
    stampdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'المنتج'
        verbose_name_plural = 'المنتجات'

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField('أسم جهه اﻷتصال', max_length=30)
    value = models.CharField('جهه التصال', max_length=300)
    stampdate = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'جهه اﻷتصال'
        verbose_name_plural = 'جهات اﻷتصال'
    def __str__(self):
        return self.name

