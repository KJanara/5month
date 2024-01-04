from django.urls import path
from . import views
urlpatterns = [
  path('test/', views.test_api_view),
  path('', views.movie_list_api_view)

]
