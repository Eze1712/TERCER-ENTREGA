from django.urls import path

app_name="Main"

urlpatterns = [
    path("", views.index, name="index"),

]