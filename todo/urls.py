from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_lists, name="all_lists"),
    path("create_list", views.create_list, name="create_list"),
    path("lists/<list_id>", views.view_list, name="view_list"),
    path('lists/<int:list_id>/add-items/', views.add_items, name='add_items'),

]