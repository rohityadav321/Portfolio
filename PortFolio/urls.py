from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    # path('insta', views.insta, name='home'),

    # path('', views.education, name='home'),
    # path('', views.skills, name='home'),
    # path('', views.projects, name='home'),


    # path('about', views.about, name="about"),
    # path('product', views.product, name="product"),
    # path('machine', views.machine, name="machine"),
    # path('contact', views.contact, name="contact"),
]
