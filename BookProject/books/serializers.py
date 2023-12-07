from rest_framework import serializers
from django.utils import timezone
from .models import BookModel,AuthorModel,SocialMediaHandleModel

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
    #publish date validator

    def validate_publication_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value

    #name validator
    def validate_title(self, value):
            prefix = "The"
            if not value.startswith(prefix):
                raise serializers.ValidationError(f'Title must start with "{prefix}"')
            return value

class SocialMediaHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaHandleModel
        fields = '__all__'

class AuthorModelSerializer(serializers.ModelSerializer):
    books=BookModelSerializer(many=True,read_only=True)
    handles=SocialMediaHandleSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = AuthorModel
        fields = '__all__'
        
    #to show names
    # hashtags = serializers.SerializerMethodField()
    # def get_hashtags(self, instance):
    #     return [hashtag.name for hashtag in instance.hashtags.all()]
