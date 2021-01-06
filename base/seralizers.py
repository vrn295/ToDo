from .models import Base
from rest_framework import serializers


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'
