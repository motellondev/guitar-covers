from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('video/<str:id>/', views.video, name='video'),
    path('tabs/', views.tabs, name='tabs'),
    path('contact/', views.contact, name='contact'),
    path('download/<str:id>/<str:fformat>/', views.download, name='download'),

]