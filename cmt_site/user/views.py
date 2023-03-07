from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
import os, json

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg, Q
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from user.models import *
from user.forms import *

# Create your views here.
# def dashboard(request):
#     return HttpResponse("Hello World!")

def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def get_controls(request):
  control_data = NIST_53_Controls.objects.all().values()
  template = loader.get_template('user/control_selection.html')

  context = {
    'controls': control_data,
  }
  return HttpResponse(template.render(context, request))


def get_controls_system_profile(request):
  # control_data = NIST_53_Controls.objects.all().values()
  control_data = NIST_53_Controls.objects.filter(
    Q(control_id="AC-1") |Q(control_id="AC-10") |Q(control_id="AC-5") |
    Q(control_id="AC-6") |Q(control_id="AT-2") |Q(control_id="AU-2") |    
    Q(control_id="AU-3") |Q(control_id="AU-6") |Q(control_id="CM-2") |
    Q(control_id="CM-8") |Q(control_id="CP-9") |Q(control_id="CP-10") |
    Q(control_id="IA-2") |Q(control_id="IA-5") |Q(control_id="PS-4") |
    Q(control_id="PS-5") |Q(control_id="RA-3") |Q(control_id="RA-5") |
    Q(control_id="SC-23") | Q(control_id="SI-10")
  )

  template = loader.get_template('user/system_compliance_profile.html')

  context = {
    'controls': control_data,
  }
  return HttpResponse(template.render(context, request))

def create_company_profile(request):
  form = CreateCompanyProfileForm(request.POST or None)
  if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
  return render(request,'user/create_profile.html',{'form':form})


def update_company_profile(request):
  form = UpdateCompanyProfileForm(request.POST or None)
  if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
  return render(request,'user/update_profile.html',{'form':form})
# Charts
# https://django-simple-charts.appseed.us/charts-file
# https://github.com/app-generator/sample-django-charts-simple
# https://www.codementor.io/@chirilovadrian360/django-charts-simple-bar-chart-displayed-in-three-ways-1cj0bu4cct
# https://testdriven.io/blog/django-charts/
# 
# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
# https://www.geeksforgeeks.org/data-visualization-using-chartjs-and-django/
# https://www.section.io/engineering-education/integrating-chart-js-in-django/