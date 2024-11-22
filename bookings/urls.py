from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookings_home, name="bookings_home"),
    path("create_booking/<booking_id>", views.create_booking, name="create_booking"),
    path("cancel_booking/<booking_id>", views.cancel_booking, name="cancel_booking"),
    path("my_bookings", views.my_bookings, name="my_bookings"),

]

"""    path("create_article", views.create_article, name="create_article"),
    path("edit_article/<article_id>", views.edit_article, name="edit_article"),
    path("delete_article/<article_id>", views.delete_article, name="delete_article"),
    path("create_comment", views.create_comment, name="create_comment"),
    path("edit_comment/<comment_id>", views.edit_comment, name="edit_comment"),
    path("<article_id>", views.view_article, name="view_article"),"""