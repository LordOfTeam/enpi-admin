from rest_framework import serializers

from backend import models


class ImageSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = models.ImageInfo
        fields = (
            'image',
        )

    def to_representation(self, instance):
        return super(ImageSerializer, self).to_representation(instance).get('image')


class PlaceListSerializer(
    serializers.ModelSerializer,
):
    image = ImageSerializer(many=True)

    class Meta:
        model = models.PlaceInfo
        fields = (
            'id',
            'name',
            'city',
            'area',
            'address',
            'guestRoomReferencePrice',
            'minMealCost',
            'image',
            'maxBallroomArea',
            'maxAllPeople',
            'roomNum'
        )


class BallRoomsSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = models.HallInfo
        fields = '__all__'


class RoomsSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = models.GuestRoom
        fields = '__all__'


class PlaceDetailSerializer(
    serializers.ModelSerializer
):
    image = ImageSerializer(many=True)
    ballrooms = BallRoomsSerializer(many=True)
    rooms = RoomsSerializer(many=True)

    class Meta:
        model = models.PlaceInfo
        fields = '__all__'
