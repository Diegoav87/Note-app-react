from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('note-list/', views.note_list, name='note-list'),
    path('note-detail/<str:pk>/', views.note_detail, name='note-detail'),
    path('note-create/', views.create_note, name='note-create'),
    path('note-update/<str:pk>/', views.update_note, name='note-update'),
    path('note-delete/<str:pk>/', views.delete_note, name='note-delete'),
]