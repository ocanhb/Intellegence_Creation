# menu_creation/urls.py (atau urls.py di apps terkait)

from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('modeling/', views.modeling_view, name='modeling'),
    path('creation/', views.creation_entry, name='creation_entry'),
    path('creation/api/', views.creation_entry_api, name='creation_entry_api'),
    path('api/get_all_models/', views.modeling_api_view, name='get_all_models'),
    path('integrasi/', views.integrasi_view, name='integrasi'),
    path('api/delete_model/<int:model_id>/', views.delete_model_entry, name='delete_model_entry'),

]
