from django.urls import path
from core.views import show_menu

app_name = 'menu'

urlpatterns = [
    path(r'^', show_menu, name='index'),
    path(r'^(\d+)', show_menu, name='index')
]
