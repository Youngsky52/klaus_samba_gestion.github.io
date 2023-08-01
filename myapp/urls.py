from django.urls import path
from myapp import views


urlpatterns = [

path('form_l', views.index, name='index'),
path('', views.form_l, name='form_l'),
path('ajouter', views.ajouter, name='ajouter'),
path('afficher', views.afficher, name='afficher'),
path('modifier/<int:id>', views.modifier, name='modifier'),
path('mise_a_j/<int:id>', views.mise_a_j, name='mise_a_j'),
path('supprimer/<int:id>', views.supprimer, name='supprimer'),
path('base/', views.base, name='base'),
]
