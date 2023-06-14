from rest_framework import serializers
from ..models.fact import Fact


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = "__all__"
