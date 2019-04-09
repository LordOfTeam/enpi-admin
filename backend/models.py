from django.db import models
from filebrowser.fields import FileBrowseField


class HallInfo(models.Model):
    class Meta:
        verbose_name = '宴会厅管理'
        verbose_name_plural = '宴会厅管理'

    tag = models.CharField(max_length=40,unique=True, verbose_name='标示')
    name = models.CharField(max_length=40, unique=True, verbose_name='宴会厅名称')
    area = models.IntegerField(verbose_name='面积', help_text='整数')
    height = models.FloatField(verbose_name='层高', help_text='浮点数')
    maxPeople = models.IntegerField(verbose_name='歌剧式人数', help_text='整数')
    kezhuoMaxPeople = models.IntegerField(verbose_name='课桌式人数', help_text='整数')
    yuanzhuoMaxTable = models.IntegerField(verbose_name='圆桌式桌数', help_text='整数')
    allDayPrice = models.IntegerField(verbose_name='全天价格', help_text='整数')
    halfDayPrice = models.IntegerField(verbose_name='半天价格', help_text='整数')

    def __str__(self):
        return self.tag + '-' + self.name


class ImageInfo(models.Model):
    class Meta:
        verbose_name = '场地图片管理'
        verbose_name_plural = '场地图片管理'

    name = models.CharField(max_length=40, unique=True, verbose_name='图片标示')
    image = FileBrowseField("Image", max_length=200, extensions=[".jpg", ".png"])

    def __str__(self):
        return self.name


class GuestRoom(models.Model):
    class Meta:
        verbose_name = '客房信息'
        verbose_name_plural = '客房信息'

    tag = models.CharField(max_length=40, verbose_name='标示')
    type = models.CharField(max_length=15, verbose_name='房型')
    bedType = models.CharField(max_length=10, verbose_name='床型')
    area = models.IntegerField(verbose_name='面积', help_text='整数')
    amount = models.IntegerField(verbose_name='数量', help_text='整数')
    network = models.CharField(max_length=5, default='有', verbose_name='宽带')
    price = models.IntegerField(verbose_name='刊例价', help_text='整数')

    def __str__(self):
        return  self.tag + '-' + self.type


class PlaceInfo(models.Model):
    class Meta:
        verbose_name = "场地管理"
        verbose_name_plural = "场地管理"

    name = models.CharField(max_length=40, unique=True, verbose_name='酒店名称')
    city = models.CharField(max_length=30, default='上海市', verbose_name='城市', help_text='默认：上海市')
    area = models.CharField(max_length=20, verbose_name='行政区域', help_text="举例： 浦东新区")
    address = models.CharField(max_length=40, verbose_name='地址')
    guestRoomReferencePrice = models.IntegerField(verbose_name='平均房价', help_text='整数')
    minMealCost = models.IntegerField(verbose_name='最低餐标', help_text='整数')
    introDoc = FileBrowseField("PDF", max_length=200, extensions=[".pdf"])
    image = models.ManyToManyField(ImageInfo, related_name='images')
    description = models.TextField(verbose_name='场地简介')
    ballrooms = models.ManyToManyField(HallInfo, related_name='ballrooms')
    rooms = models.ManyToManyField(GuestRoom, related_name='rooms')

    def __str__(self):
        return self.name
