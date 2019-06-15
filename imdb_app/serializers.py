from rest_framework import exceptions
from rest_framework import serializers
from .models import Movie, Genre
class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """

    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')

    def create(self, validated_data):

        validated_data = dict(validated_data)
        check_name = validated_data.get('name')
        if check_name:
            genre_later = validated_data.pop('genre') if validated_data.get('genre') else []
            new_movie, update = Movie.objects.update_or_create(name=validated_data.get('name'), defaults=validated_data)
            new_movie.save()
            validated_data['genre'] = genre_later
            for name in validated_data['genre']:
                obj, created = Genre.objects.get_or_create(name=name)
                new_movie.genre.add(obj)
            return new_movie
        else:
            raise exceptions.ValidationError({
                'name': 'This field is required.'
            })

    def to_internal_value(self, data):
        data = dict(data)
        op = {i: v[0] if i != "genre" else v for i, v in data.items() if v[0]}
        
        return op



        
