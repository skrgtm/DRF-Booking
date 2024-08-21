from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    image_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'property_type',
            'location',
            'post_type',
            'bhk_type',
            'cost',
            'description',
            'images',
            'image_ids',
            'posted_by',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        image_ids = validated_data.pop('image_ids', [])
        property_instance = Property.objects.create(**validated_data)
        if image_ids:
            images = PropertyImage.objects.filter(id__in=image_ids)
            property_instance.images.set(images)
        return property_instance
