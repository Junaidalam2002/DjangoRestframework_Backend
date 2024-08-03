from django.urls import path
from .views import DataViewset


urlpatterns = [
    path('data/', DataViewset.as_view()),
    path('data/<int:id>', DataViewset.as_view())
]