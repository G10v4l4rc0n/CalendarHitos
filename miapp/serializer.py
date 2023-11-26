from rest_framework import serializers
from .models import Hito

class HitoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model=Hito
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['todo_el_dia'] = bool(data['todo_el_dia'])
        return data
    def create(self, validated_data):
        hito = Hito.objects.create(**validated_data)
        if hito.todo_el_dia:
            hito.fecha_termino = None
            hito.save()
        return hito

