from django.urls import path
from api_creation.views import (
 
    EngineeringDataAPIView,
    DatasetRequestAPIView,
    DatasetResponseAPIView,
    ProjectModelAPIView,
    FinalModelAPIView,
    APIRootView,
)

from . import views

urlpatterns = [
    path('integrasi/', views.integrasi_view, name='integrasi-view'),
    path('submit-engineering/', views.submit_engineering, name='submit_engineering_data'),
    path('submit-dataset-request/', views.submit_dataset_request, name='submit_dataset_request'),
    path('submit-dataset-response/', views.submit_dataset_response, name='submit_dataset_response'),
    path('submit-project-model/', views.submit_project_model, name='submit_project_model'),
    path('submit-final-model/', views.FinalModel, name='submit_final_model'),
    
    path('laporan-integrasi/', views.laporan_integrasi_view, name='laporan_integrasi'),

    path('engineering/edit/<int:pk>/', views.edit_engineering, name='edit_engineering'),
    path('engineering/delete/<int:pk>/', views.delete_engineering, name='delete_engineering'),

    path('dataset/edit/<int:pk>/', views.edit_dataset, name='edit_dataset'),
    path('dataset/delete/<int:pk>/', views.delete_dataset, name='delete_dataset'),

    path('project/edit/<int:pk>/', views.edit_project_model, name='edit_project_model'),
    path('project/delete/<int:pk>/', views.delete_project_model, name='delete_project_model'),

    path('final/edit/<int:pk>/', views.edit_final_model, name='edit_final_model'),
    path('final/delete/<int:pk>/', views.delete_final_model, name='delete_final_model'),

    path('', APIRootView.as_view(), name='api-root'),
    path('engineering-data/', EngineeringDataAPIView.as_view(), name='engineering-data'),
    path('dataset-request/', DatasetRequestAPIView.as_view(), name='dataset-request'),
    path('dataset-response/', DatasetResponseAPIView.as_view(), name='dataset-response'),
    path('project-model/', ProjectModelAPIView.as_view(), name='project-model'),
    path('final-model/', FinalModelAPIView.as_view(), name='final-model'),
]
