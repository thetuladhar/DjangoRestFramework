from rest_framework import serializers
from .models import Person

def validate_age(value):
    if value <= 0:
        raise serializers.ValidationError("Age must be greater than zero.")
    return value

def validate_unique_email(value):
    if Person.objects.filter(email=value).exists():
        raise serializers.ValidationError("This email address is already in use.")
    return value
    