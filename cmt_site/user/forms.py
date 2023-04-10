from .models import Company_Profile
from django import forms
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class CreateCompanyProfileForm(forms.ModelForm):
    system_choices = [('Applications','Applications'), ('Servers','Servers'), ('Laptops/Desktops','Laptops/Desktops'), 
                    ('Network Devices','Network Devices'), ('Databases','Databases'), ('Containers','Containers'),
                    ('Unified Endpoint Management', 'Unified Endpoint Management')]
    iniital_choices = ['Applications', 'Servers', 'Laptops/Desktops', 'Network Devices', 
                    'Databases', 'Containers', 'Unified Endpoint Management']
    systems  = forms.MultipleChoiceField(
        choices = system_choices,
        initial = iniital_choices,
        label = '<br />Systems:', 
        widget = forms.CheckboxSelectMultiple, 
        required = True)

    certification_requirements_choices = [('CMMC Level 1','CMMC Level 1'), ('CMMC Level 2','CMMC Level 2'), 
                    ('CMMC Level 3','CMMC Level 3'), ('None', 'None')]
    certification_requirements  = forms.ChoiceField(
        choices = certification_requirements_choices,
        label = '<br />Certification Requirements:', 
        widget = forms.Select(attrs={'class': 'form-control'}),
        initial = 'CMMC Level 3', 
        required = True
    )

    name = forms.CharField(required = True, label = '<br />Company Name:')

    groups_bool = [('Yes','Yes'), ('No','No')]
    groups  = forms.ChoiceField(
        choices = groups_bool,
        label = '<br />Company Sub-groups:', 
        widget = forms.Select(attrs={'id': 'group', 'onchange': 'display_group_input()'}),
        initial = 'No', 
        required = True
    )

    class Meta:
        model  = Company_Profile
        fields = '__all__'

class UpdateCompanyProfileForm(forms.ModelForm):
    system_choices = [('Applications','Applications'), ('Servers','Servers'), ('Laptops/Desktops','Laptops/Desktops'), 
                    ('Network Devices','Network Devices'), ('Databases','Databases'), ('Containers','Containers'),
                    ('Unified Endpoint Management', 'Unified Endpoint Management')]
    iniital_choices = ['Applications', 'Servers', 'Laptops/Desktops', 'Network Devices', 
                    'Databases', 'Containers', 'Unified Endpoint Management', 'RTOS']
    systems  = forms.MultipleChoiceField(
        choices = system_choices,
        initial = iniital_choices,
        label = '<br />Systems:', 
        widget = forms.CheckboxSelectMultiple, 
        required = True)

    certification_requirements_choices = [('CMMC Level 1','CMMC Level 1'), ('CMMC Level 2','CMMC Level 2'), 
                    ('CMMC Level 3','CMMC Level 3'), ('None', 'None')]
    certification_requirements  = forms.ChoiceField(
        choices = certification_requirements_choices,
        label = '<br />Certification Requirements:', 
        widget = forms.Select(attrs={'class': 'form-control'}),
        initial = 'CMMC Level 3', 
        required = True
    )

    name = forms.CharField(required = True, label = '<br />Company Name:', initial='Vaporware')

    groups_bool = [('Yes','Yes'), ('No','No')]
    groups  = forms.ChoiceField(
        choices = groups_bool,
        label = '<br />Company Sub-groups:', 
        widget = forms.Select(attrs={'id': 'group', 'onchange': 'display_group_input()'}),
        initial = 'No', 
        required = True
    )

    class Meta:
        model  = Company_Profile
        fields = '__all__'