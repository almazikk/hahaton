"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title='WorkNet',
        description='WorkNet - это удобная и современная онлайн-платформа,'
                    'предназначенная для помощи работникам и работодателям '
                    'в поиске и предоставлении рабочих возможностей.',
        default_version='v1'
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('resume.urls')),
    path('api/v1/', include('vacancy.urls')),
    path('api/v1/', include('review.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjU2NzA5MywiaWF0IjoxNjk5OTc1MDkzLCJqdGkiOiIzNWM2M2RmZWU1YWQ0YmJlOGIzNWQxYjgzMzlmY2YwZCIsInVzZXJfaWQiOjJ9.kfBvjDnRq8-49trUlQpvwfD9HdzYVkmvZ8aXnvPvkx0",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMjcxMDkzLCJpYXQiOjE2OTk5NzUwOTMsImp0aSI6IjNhNzI3ZTBmODUyMDQzMjI5NjNlZjY4MGY4MWFlNzA0IiwidXNlcl9pZCI6Mn0.lM8TBwai0lak_YGeGZH9W-U4vbSC6zIO90MbwvEAbks"
# }