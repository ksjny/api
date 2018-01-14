from logit import views

from rest_framework import routers
from dynamic_rest.routers import DynamicRouter

from django.urls import include, path

router = DynamicRouter()

router.register('users', views.UserViewSet)
router.register('diagnosis', views.DiagnosisViewSet)
router.register('medication', views.MedicationViewSet)
router.register('symptom', views.SymptomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('classify/<int:user_id>', views.classify),
    path('users/me/', views.UserViewSet.as_view({'get': 'retrieve'}), kwargs={'pk': 'me'}),
]
