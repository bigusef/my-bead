from django.db import models


class Mattress(models.Model):
    name = models.CharField('اﻷسم اﻷنجليزي', max_length=50)
    verbose_name = models.CharField('اﻷسم العربي', max_length=50)
    description = models.TextField('الوصف')
    features = models.TextField('المميزات')
    # cover = models.ImageField(uplodeto='mattress')
    is_new = models.BooleanField('إظهار في الصفحه الرئيسيه', default=False)
    stampdate = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

