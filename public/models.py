from django.db import models
from django.core.validators import RegexValidator


class Telephones(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="لابد ان يكون رقم هاتف حقيقي")

    title = models.CharField(max_length=25, unique=True, verbose_name='أسم رقم الهاتف')
    number = models.CharField(max_length=15, verbose_name='رقم الهاتف', validators=[phone_regex])

    class Meta:
        verbose_name = 'الهاتف'
        verbose_name_plural = 'أرقام الهاتف'

    def __str__(self):
        return self.title


class Emails(models.Model):
    title = models.CharField(max_length=25, verbose_name='اﻷسم')
    email = models.EmailField(unique=True, verbose_name='البريد اﻷلكتروني')

    class Meta:
        verbose_name = 'البريد اﻷلكتروني'
        verbose_name_plural = 'البريد اﻷلكتروني'

    def __str__(self):
        return self.title


class Addresses(models.Model):
    title = models.CharField(max_length=25, unique=True, verbose_name='اﻷسم')
    address = models.TextField(verbose_name='العنوان')

    class Meta:
        verbose_name = 'العنوان'
        verbose_name_plural = 'العناوين'

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    about_word = models.TextField(verbose_name='كلمه عن الشركه')
    facebook = models.CharField(max_length=300, verbose_name='رابط صفحه الفيس بوك')
    instagram = models.CharField(max_length=300, verbose_name='رابط صفحه الإنستجرام')
    telephones = models.ManyToManyField(Telephones, verbose_name='الهواتف')
    emails = models.ManyToManyField(Emails, verbose_name='البريد اﻷلكتروني')
    addresses = models.ManyToManyField(Addresses, verbose_name='العناوين')

    class Meta:
        verbose_name = 'البيانات العامه'
        verbose_name_plural = 'البيانات العامه'

    def __str__(self):
        return 'بيانات الشركه'


class Mattress(models.Model):
    name = models.CharField(max_length=50, verbose_name='أسم المرتبه')
    description = models.TextField(verbose_name='وصف المرتبه')
    features = models.TextField(verbose_name='المميزات', help_text="يجب إدخال كل ميزه مفصول بينها بعلامه ','")
    cover = models.ImageField(upload_to='mattress', verbose_name='صوره المرتبه')
    color = models.CharField(max_length=7, verbose_name='لون القائمه')
    is_new = models.BooleanField(verbose_name='إظهار في الصفحه الرئيسيه', default=False)
    stamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'المرتبه'
        verbose_name_plural = 'المراتب'

    def __str__(self):
        return self.name

    def get_features_list(self):
        self.result = self.features.split(',')
        for i in self.result:
            if len(i) <= 2:
                self.result.remove(i)
        return self.result


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='أسم المنتج')
    description = models.TextField(verbose_name='مواصفات المنتج')
    features = models.TextField(verbose_name='المميزات', help_text="يجب إدخال كل ميزه مفصول بينها بعلامه ','")
    cover = models.ImageField(upload_to='product', verbose_name='صوره المنتج')
    color = models.CharField(max_length=7, verbose_name='لون القائمه')
    is_new = models.BooleanField(verbose_name='إظهار في الصفحه الرئيسيه', default=False)
    stamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'المنتج'
        verbose_name_plural = 'المنتجات'

    def __str__(self):
        return self.name

    def get_features_list(self):
        self.result = self.features.split(',')
        for i in self.result:
            if len(i) <= 2:
                self.result.remove(i)
        return self.result


class Manufacturer(models.Model):
    text = models.CharField(max_length=200, unique=True, verbose_name='أسم المنتج')

    class Meta:
        verbose_name = 'منتج مستلزمات تصنيع'
        verbose_name_plural = 'مستلزمات التصنيع'

    def __str__(self):
        return self.text
