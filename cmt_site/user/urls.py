from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('dashboard', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('create_profile', views.create_company_profile, name='create_profile'),
    path('update_profile', views.update_company_profile, name='update_profile'),
    path('control_selection', views.get_controls, name='control_selection'),
    path('systems', TemplateView.as_view(template_name='user/list_systems.html'), name='systems'),
    path('system_compliance_profile', views.get_controls_system_profile, name='system_compliance_profile'),
    path('settings', TemplateView.as_view(template_name='user/settings.html'), name='settings'),
    path('setup', TemplateView.as_view(template_name='user/setup.html'), name='setup'),
    path('view', TemplateView.as_view(template_name='user/view.html'), name='view'),
    path('population-chart/', views.population_chart, name='population-chart'),
]