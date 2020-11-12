from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get-data/', views.get_data, name='get_data'),
    path('summarized/', views.summarize_data, name="summarize"),
    path('previously-summarized/', views.prev_summarize_data, name="previously_summarized"),
]
