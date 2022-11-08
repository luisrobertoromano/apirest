from django.urls import path
from . import views

app_name = "crud_app"

urlpatterns = [
    path(
        'lista/',
        views.PersonaListView.as_view(),
        name='lista-personas'
    ),
    path(
        'api/lista/',
        views.PersonListApiView.as_view(),
        name='lista-api'
    ),
]