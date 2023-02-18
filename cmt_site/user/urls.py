from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('dashboard', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('control_selection', TemplateView.as_view(template_name='user/control_selection.html'), name='control_selection'),
    path('settings', TemplateView.as_view(template_name='user/settings.html'), name='settings'),
    path('setup', TemplateView.as_view(template_name='user/setup.html'), name='setup'),
    path('view', TemplateView.as_view(template_name='user/view.html'), name='view'),
    path('population-chart/', views.population_chart, name='population-chart'),
]