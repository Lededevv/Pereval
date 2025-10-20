from rest_framework import serializers
from .models import CustomUser, Pereval_added, Coords, Images, Level
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CustomUserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'last_name', 'first_name', 'otc', 'phone', 'username']
        extra_kwargs = {'email': {'validators': []}}


class ImagesSerializer(WritableNestedModelSerializer):
    # data = serializers.CharField(write_only=True)

    class Meta:
        model = Images
        fields = ['title', 'data']


class LevelSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class PerevalSerializer(WritableNestedModelSerializer):
    user = CustomUserSerializer()
    status = serializers.CharField(read_only=True)
    images = ImagesSerializer(many=True, )
    level = LevelSerializer()
    coords = CoordsSerializer()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        method = kwargs.get('context', {}).get('request').method
        if method == 'PATCH' or method == 'PUT':
            # Если идет обновление, устанавливаем поле readonly
            self.fields['user'].read_only = True
        elif method == 'POST':
            # При создании оставляем доступ для записи
            self.fields['user'].read_only = False

    class Meta:
        model = Pereval_added
        fields = [
            'beauty_title', 'title',
            'other_titles', 'connect',
            'add_time', 'status',
            'user', 'level',
            'coords', 'images',
        ]

    def update(self, instance, validated_data):

        validated_data.pop('status', None)
        validated_data.pop('add_time', None)

        return super().update(instance, validated_data)

    def create(self, validated_data):
        level_data = validated_data.pop('level', {})
        user_data = validated_data.pop('user', {})
        coords_data = validated_data.pop('coords', {})
        images_data = validated_data.pop('images', [])

        user, _ = CustomUser.objects.get_or_create(email=user_data['email'], defaults=user_data)
        coords = Coords.objects.create(**coords_data)
        pereval = Pereval_added.objects.create(user=user, coords=coords, **validated_data)
        level = Level.objects.create(pereval=pereval, **level_data)

        for image_item in images_data:
            title_img = image_item["title"]
            data_img = image_item["data"]  # Предположительно InMemoryUploadedFile
            new_image = Images.objects.create(
                pereval=pereval,
                title=title_img,
                data=data_img
            )
        return pereval
