from django.contrib import admin

from backend.models import *


class GuestRoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tag',
        'type',
        'bedType',
        'area',
        'amount',
        'network',
        'price'
    )
    search_fields = (
        'id',
        'tag',
        'type',
        'bedType',
        'area',
        'amount',
        'network',
        'price'
    )


class PlaceInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'city',
        'area',
        'address',
        'maxBallroomArea',
        'maxAllPeople',
        'roomNum'
    )
    search_fields = (
        'id',
        'name',
        'city',
        'area',
        'address',
        'maxBallroomArea',
        'maxAllPeople',
        'roomNum'
    )

    filter_horizontal =(
        'image',
        'ballrooms',
        'rooms'
    )


class HallInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tag',
        'name',
        'area',
        'height',
        'maxPeople',
        'kezhuoMaxPeople',
        'yuanzhuoMaxTable',
        'allDayPrice',
        'halfDayPrice'
    )
    search_fields = (
        'id',
        'tag',
        'name',
        'area',
        'height',
        'maxPeople',
        'kezhuoMaxPeople',
        'yuanzhuoMaxTable',
        'allDayPrice',
        'halfDayPrice'
    )


class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(PlaceInfo, PlaceInfoAdmin)
admin.site.register(HallInfo, HallInfoAdmin)
admin.site.register(GuestRoom, GuestRoomAdmin)
admin.site.register(ImageInfo, ImageInfoAdmin)
