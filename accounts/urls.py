from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # ...
    path('suporte/', inicio, name='index'),
    path('cadastra-adm/', cadastro, name='cadastro_template'),
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),
    path('cadastrando/', cadastrando, name='cadastrando'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
