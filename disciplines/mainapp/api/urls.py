from rest_framework.routers import DefaultRouter

from .api_views import (
    DisciplineViewSet,
    GroupViewSet,
    StudentViewSet,
    MarkViewSet,
    TeacherViewSet,
)

app_name = ''

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'marks', MarkViewSet, basename='mark')
router.register(r'disciplines', DisciplineViewSet, basename='discipline')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
] + router.urls
