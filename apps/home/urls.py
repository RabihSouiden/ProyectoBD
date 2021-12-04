from django.urls import path, re_path
from apps.home import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this
urlpatterns = [

    # The home page
    path('', views.index_admin, name='home'),

    path('propietarios', views.index_propietario, name='home_propietario'),

    path('veterinaria', views.index_veterinaria, name='home_veterinaria'),

    path('social', views.social_propietario, name='social_propietario'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)