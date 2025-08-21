from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("", views.note_list, name="note_list"),
    path("create/", views.note_create, name="note_create"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("<int:pk>/edit/", views.note_update, name="note_update"),
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),
    path("tags/create/", views.tag_create, name="tag_create"),
    path("categories/create/", views.category_create, name="category_create"),
]
