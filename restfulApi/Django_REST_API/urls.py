from django.urls import path
from .views import DataViewset


urlpatterns = [
    path('api/', DataViewset.as_view()),
    path('api/<int:id>', DataViewset.as_view())
]