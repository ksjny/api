from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'logit'
urlpatterns = [
    url('api/authenticate$', views.authenticateuser, name="authenticateuser"),
    url('api/logout$', views.signout, name="signout"),

    url('api/users$', views.user, name="user"),
    url('api/users/([0-9]+)$', views.user_id, name="user_id"),

    url('api/symptoms$', views.symptom, name="symptom"),
    url('api/symptoms/([0-9]+)$', views.symptom_id, name="symptom_id"),

    url('api/medications$', views.medication, name="medication"),
    url('api/medications/([0-9]+)$', views.medication_id, name="medication_id"),
]

handler404 = 'views.custom404'
