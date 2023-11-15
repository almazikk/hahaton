from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import generics, ModelViewSet
from rest_framework.views import APIView
from .serializers import VacancySerializer, ApplyToVacancySerializer, EmployerResumeSerializer, UpdateResumeStatusSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsEmployer
from rest_framework.response import Response
from .utils import send_about_resume
from resume.models import Resume
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Vacancy
from rest_framework.exceptions import NotFound
from slugify import slugify



User = get_user_model()


class PermissionMixin:
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsEmployer]
        return super().get_permissions()


class VacancyViewSet(PermissionMixin, ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'salary', 'requirements']
    search_fields = ['title', 'company_title', 'company_descr', 'salary', 'requirements']

    @method_decorator(cache_page(60*5))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, *kwargs)

    def perform_create(self, serializer):
        serializer.save(who_created=self.request.user)


class ApplyToVacancyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print("ApplyToVacancyView is called.")
        print(request.data)

        serializer = ApplyToVacancySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        slug = slugify(str(serializer.validated_data['slug']))
        print(f"Trying to get vacancy with slug: {slug}")

        try:
            vacancy = Vacancy.objects.get(slug=slug)
        except Vacancy.DoesNotExist:
            raise NotFound('Такой вакансии не существует')

        resume = get_object_or_404(Resume, user=request.user)

        vacancy.applicants.add(request.user)
        resume.applied_vacancies.add(vacancy)
        send_about_resume(vacancy.who_created.email)

        print("Application successful.")
        return Response('Ваше резюме успешно подано, ожидайте обратной связи от работодателя')


class EmployerGetResumeView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsEmployer]
    serializer_class = EmployerResumeSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        vacancy = get_object_or_404(Vacancy, slug=slug)

        # Получаем связанные резюме через таблицу промежуточных связей
        resumes = Resume.objects.filter(applied_vacancies=vacancy)

        return resumes


class UpdateResumeStatusView(APIView):
    def post(self, request, resume_id, *args, **kwargs):
        resume = get_object_or_404(Resume, id=resume_id)
        if not resume.applied_vacancies.filter(who_created=request.user).exists():
            return Response('У вас нет разрешения на изменение статуса этого резюме.')

        serializer = UpdateResumeStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'status' not in request.data:
            return Response('Отсутствует параметр "status" в теле запроса.')
        resume.status = serializer.validated_data['status']
        resume.save()
        return Response(f'Статус резюме успешно обновлен на "{resume.get_status_display()}".')