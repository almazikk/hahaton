from django.urls import path, include
from .views import FavoritesView, FavoritesListView, RecommendedVacanciesView

urlpatterns = [
    path('favorites/<slug:slug>/', FavoritesView.as_view()),
    path('favorites/', FavoritesListView.as_view()),
    path('recommended_vacancies/', RecommendedVacanciesView.as_view(), name='recommended_vacancies'),

]