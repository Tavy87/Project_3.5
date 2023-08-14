from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('widget/add/', views.add_widget, name='add_widget'),
    path('widget/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete_widget'),
]