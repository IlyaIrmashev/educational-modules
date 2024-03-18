from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    qty_modules = serializers.SerializerMethodField()

    def get_qty_modules(self, instance):
        return instance.module.count()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone_num', 'qty_modules')
