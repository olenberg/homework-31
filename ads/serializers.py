from users.models import User
from .models import Ad, Category
from rest_framework import serializers


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Category.objects.all()
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop('author')
        self._category = self.initial_data.pop('category')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        ad.save()
        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField(required=False)
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._category = self.initial_data.pop('category')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        ad.save()

        return ad


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]
