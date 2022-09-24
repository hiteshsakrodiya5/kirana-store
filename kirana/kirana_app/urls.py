from django.urls import path
from . import views
urlpatterns = [
    path("addItem/", views.AddItem.as_view(), name="add_item"),
]