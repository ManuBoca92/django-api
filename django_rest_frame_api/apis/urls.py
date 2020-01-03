from django.conf.urls import url
from rest_framework import routers
from .views import CityViewSet, UsersViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'users', UsersViewSet)

schema_view = get_swagger_view(title='Poland users API')

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'docs/', schema_view)
]
urlpatterns += router.urls
