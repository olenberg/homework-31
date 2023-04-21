from users.models import User
from .models import Ad, Category
from rest_framework import serializers


class AdsListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"
