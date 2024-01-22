from django.contrib import admin
from django.urls import path, include
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentApi.as_view()),
    path('studentapi/<int:pk>/',views.StudentApi.as_view()),
]
