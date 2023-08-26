from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('captcha', views.index, name='captcha'),

    # ... other URL patterns ...

]