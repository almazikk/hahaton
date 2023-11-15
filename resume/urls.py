from rest_framework.urls import path
from .views import ResumeView, ResumeDetailView


urlpatterns = [
    path('resume/', ResumeView.as_view()),
    path('resume/<int:pk>/', ResumeDetailView.as_view()),
    # path('employer_retrieve_resume/<slug:slug>/', EmployerResumeRetrieveView.as_view()),

]

