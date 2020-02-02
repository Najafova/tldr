from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
    # path('register/', register, name="register"),
    path('post/<int:pk>/', post_by_tag, name="post_by_tag"),
    path('about/', about, name='about'),
    path('404/', error_page, name='error_page'),
    path('contact/', contact, name='contact'),
    path('add_tldr/', add_tldr, name='add_tldr'),

]