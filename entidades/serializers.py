from rest_framework import serializers
from entidades.models import Maestro, Salon


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'


class SalonMinSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Salon
        fields = ('id', 'codigo', 'letra')


class MaestroSerializer(serializers.ModelSerializer):
    salones = SalonMinSerializer(many=True)
    class Meta:
        model = Maestro
        fields = '__all__'
    
    def create(self, validated_data):
        salones = validated_data.pop('salones')
        maestro = Maestro.objects.create(**validated_data)
        for salon in salones:
            Salon.objects.create(**salon, maestro=maestro)
        return maestro
    
    def update(self, instance, validated_data):
        salones = validated_data.pop('salones')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # for salon in salones:
        #     for attr, value in salon.items():
        #         setattr(salon, attr, value)
        return instance
