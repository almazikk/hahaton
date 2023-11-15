from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField, Serializer, SlugField, CharField
from .models import Vacancy
from django.contrib.auth import get_user_model
from slugify import slugify
from resume.models import Resume


User = get_user_model()


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'email']


class VacancySerializer(ModelSerializer):
    who_created = ReadOnlyField(source='user')
    title = CharField(max_length=50)

    class Meta:
        model = Vacancy
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['who_created'] = user
        return super(VacancySerializer, self).create(validated_data)


class ApplyToVacancySerializer(Serializer):
    slug = SlugField()

    def validate_slug(self, value):
        try:
            vacancy = Vacancy.objects.get(slug=value)
        except Vacancy.DoesNotExist:
            raise ValidationError('Такой вакансии не существует')
        return vacancy


class EmployerResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        exclude = ['applied_vacancies']


class UpdateResumeStatusSerializer(Serializer):
    status = CharField()

    def validate_status(self, value):
        allowed_statuses = ['viewed', 'rejected', 'contact_soon']

        if value not in allowed_statuses:
            raise ValidationError(
                f'Недопустимое значение статуса. Допустимые значения: {", ".join(allowed_statuses)}')

        return value