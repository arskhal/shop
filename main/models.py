from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=2000)
    price = models.IntegerField('Цена')
    img = models.ImageField('Картинка',upload_to='products',blank=True)

    def get_img(self):
        if self.img:
            return self.img.url
        else:
            return '/static/default.png'

    def __str__(self):
        # return "{0.title} {0.price}".format(self) 
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

