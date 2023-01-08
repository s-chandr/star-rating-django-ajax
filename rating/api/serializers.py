from rest_framework import serializers
from main.models import Book,BookReview

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'