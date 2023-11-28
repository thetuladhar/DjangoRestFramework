from rest_framework import serializers
from .models import Person, Address
from .validators import validate_age, validate_unique_email

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    age = serializers.IntegerField(validators=[validate_age])
    email = serializers.EmailField(validators=[validate_unique_email])

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email', 'address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_instance = Address.objects.create(**address_data)
        person_instance = Person.objects.create(address=address_instance, **validated_data)
        return person_instance

   