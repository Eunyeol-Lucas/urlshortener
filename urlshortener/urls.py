from django.urls import path
from . import views

app_name='shortener'
urlpatterns = [
    path('urls/', views.index, name='index'),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect'),
]
