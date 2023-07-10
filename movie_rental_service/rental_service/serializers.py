from .models import Movie
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError
from datetime import date


class MovieSerializer(serializers.ModelSerializer):

    Title = serializers.CharField(
        required=True,
        max_length=100,
        min_length=8,
        validators=[
            UniqueValidator(queryset=Movie.objects.all(),message=" Title already exists"),
        ],
    )
    Release_date = serializers.DateField(required=True)
    Genre = serializers.ChoiceField(choices=["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"],required=True)
    Duration_minutes = serializers.IntegerField(min_value=1, max_value=600,required=True)
    Rating = serializers.FloatField(min_value=0.0, max_value=10.0, required=False)


    def validate_Title(self, data):
        prefix = "Movie-"
        if not data.startswith(prefix):
            raise ValidationError("Title must start with 'Movie-' prefix")
        text = data[len(prefix):]
        if len(text) < 2 or len(text) > 100:
            raise ValidationError("Title text must be : between 2 and 100 characters long")
        return data


    def validate_Release_date(self, data):
        if data > date.today():
            raise serializers.ValidationError("Release date cannot be in the future")
        if data < date.today().replace(year=date.today().year - 30):
            raise serializers.ValidationError("Release date should be within the last 30 years")
        return data


    def validate_Genre(self, data):
        choices=["Action", "Drama", "Comedy", "Thriller", "Sci-Fi"]
        if data not in choices:
            raise ValidationError("Genre must be : Action, Drama, Comedy, Thriller, Sci-Fi")
        return data


    def validate_Duration_minutes(self, data):
        if data < 1 or data > 600:
            raise ValidationError("Duration_minutes must be : between 1 and 600 minutes (10 hours)")
        return data


    def validate_Rating(self, data):
        if data < 0.0 or data > 10.0 :
            raise ValidationError(" validate_Rating must be : between 0.0 and 10.0 (Decimal number)")
        return data

    class Meta:
        model = Movie
        fields = ['Title','Release_date','Genre','Duration_minutes','Rating']
