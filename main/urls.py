from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('contact/', views.contact, name='contact'),

]