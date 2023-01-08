from django.urls import path
from . import views
# from django.conf.urls import handler404, handler500

app_name = 'sneakers'
urlpatterns = [
 # Home page.
 path('', views.get_all_sneakers, name='get_all_sneakers'),
 path('products/<int:product_id>/', views.get_sneaker_details, name='get_sneaker_details'),
]

# handler404 = views.error_404
# handler500 = views.error_500