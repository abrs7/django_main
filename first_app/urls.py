from django.urls import path
from first_app import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('users', views.users, name = 'users'),
    path('forms', views.form_name_view, name = 'form_name_view'),
    path('others', views.others, name="others"),


]