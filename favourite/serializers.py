from rest_framework import serializers
from .models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        unique_together = [("user", "product")]
        model = Favourite
        fields = '__all__'