from django.urls import path
from . import views
app_name = 'sneakers'
urlpatterns = [
 # Home page.
 path('', views.get_all_sneakers, name='get_all_sneakers'),
]