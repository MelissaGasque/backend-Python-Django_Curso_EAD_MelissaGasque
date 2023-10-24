from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "username",
            "password",
            "is_superuser"
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data: dict) -> Account:
        is_superuser = validated_data.get("is_superuser", False)

        if is_superuser:
            return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
