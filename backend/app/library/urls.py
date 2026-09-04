from django.urls import path
from .views import LibroAPIView, LibrosRetrieve

urlpatterns = [
    path('alta/', LibroAPIView.as_view(),),
    path('lista/', LibrosRetrieve.as_view(),),
]