from rest_framework import serializers
from .models import Burger


class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = ['title', 'price', 'image']

    def to_representation(self, instance):
        representation = super(BurgerSerializer, self).to_representation(instance)
        representation['description'] = f'{representation["title"]}!\n\nЦена: {representation["price"]}₸'
        return representation