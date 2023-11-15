from django.db import models
from django.contrib.auth import get_user_model
from vacancy.models import Vacancy

User = get_user_model()


class Favorites(models.Model):
    user = models.ForeignKey(User, related_name='favorite', on_delete=models.CASCADE)
    favorite_vacancy = models.ForeignKey(Vacancy, related_name='favorite_vacancy', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'favorite_vacancy']