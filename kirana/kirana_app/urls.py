from django.urls import path
from . import views
urlpatterns = [
    path("addItem/", views.AddItem.as_view(), name="add_item"),
    path("allItem/", views.ListViewItem.as_view(), name="all_item"),
    path("itemDetail/<str:item_id>/", views.DetailItem.as_view(), name="detail_item"),
]