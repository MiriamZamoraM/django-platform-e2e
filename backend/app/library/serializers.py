from rest_framework import serializers
from .models import Libros


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ('id', 'nombre', 'autor', 'isbn', 'edicion', 'fecha_pub', 'creado')

        def create(self, validated_data):

            libros = Libros.objects.create(**validated_data)

            return libros