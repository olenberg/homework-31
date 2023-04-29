from users.models import User
from ads.models import Ad
from .models import Selection
from rest_framework import serializers


class SelectionListSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    items = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        queryset=Selection.objects.all(),
        many=True
    )

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'



class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    items = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        queryset=Selection.objects.all(),
        many=True
    )

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
