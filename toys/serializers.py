from rest_framework.serializers import ModelSerializer
from .models import Toy

class ToySerializer(ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id',
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_included_in_home')




"""
# Esta es la forma manual de usar el Serializer y colocar 1 a 1 los elementos que queremos serializar de nuestra base de datos.
# Adicionalmente, de esta forma debemos sobre escribir los métodos create and update y repitiendo mucho código.

from rest_framework import serializers


class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Toy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.toy_category = validated_data.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance

"""