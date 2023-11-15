from rest_framework import serializers
from .models import Favorites
from vacancy.models import Vacancy


class FavoriteVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title', 'requirements']


class FavoritesSerializer(serializers.ModelSerializer):
    vacancy_title = serializers.CharField(source='favorite_vacancy.title', read_only=True)
    vacancy_resp = serializers.CharField(source='favorite_vacancy.responsibilities', read_only=True)

    class Meta:
        model = Favorites
        fields = ['vacancy_title', 'vacancy_resp']


