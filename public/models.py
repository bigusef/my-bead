from django.db import models
from django.core.validators import RegexValidator


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


class Telephones(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="لابد ان يكون رقم هاتف حقيقي")
    title = models.CharField('اﻷسم', max_length=25)
    number = models.CharField('رقم الهاتف', validators=[phone_regex], max_length=15, unique=True)
    
    class Meta:
        verbose_name = 'الهاتف'
        verbose_name_plural = 'ارقام التلفون'

    def __str__(self):
        return self.title


class Emails(models.Model):
    title = models.CharField('اﻷسم', max_length=25)
    email = models.EmailField('البريد اﻷلكتروني')
    
    class Meta:
        verbose_name = 'البريد اﻷلكتروني'
        verbose_name_plural = 'البريد اﻷلكتروني'

    def __str__(self):
        return self.title


class Adresses(models.Model):
    title = models.CharField('اﻷسم', max_length=25)
    adress = models.TextField('العنوان')

    class Meta:
        verbose_name = 'العنوان'
        verbose_name_plural = 'العناوين'

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    about_word = models.TextField('كلمه عن الشركه')
    telephones = models.ManyToManyField(Telephones, verbose_name='الهواتف')
    emails = models.ManyToManyField(Emails, verbose_name='البريد اﻷلكتروني')
    adresses = models.ManyToManyField(Adresses, verbose_name='العناوين')
    
    class Meta:
        verbose_name = 'البيانات العامه'
        verbose_name_plural = 'البيانات العامه'

    def __str__(self):
        return 'بيانات الشركه'

