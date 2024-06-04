from rest_framework.routers import DefaultRouter

from django.urls import include, path
from assignments import views

router=DefaultRouter()
router.register('assignments',views.GetAssignmentsViewSet)

app_name = 'assignments'
urlpatterns = [
    path('', include(router.urls)),
]