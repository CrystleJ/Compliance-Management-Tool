from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

class NIST_171_Controls(models.Model):
    family = models.CharField(max_length=250, null=True, blank=True)
    control_id = models.CharField(max_length=30, primary_key=True)
    control_txt = models.TextField(null=True, blank=True)
    discussion = models.TextField(null=True, blank=True)

class NIST_172_Controls(models.Model):
    family = models.CharField(max_length=250, null=True, blank=True)
    control_id = models.CharField(max_length=30, primary_key=True)
    control_txt = models.TextField(null=True, blank=True)
    discussion = models.TextField(null=True, blank=True)

class NIST_53_Controls(models.Model):
    control_name = models.CharField(max_length=200)
    control_id = models.CharField(max_length=30, primary_key=True)
    control_txt = models.TextField(null=True)
    discussion = models.TextField(null=True)
    cmmc_level = models.PositiveIntegerField(null=True)
    control_id_171 = models.TextField(null=True)
    control_id_172 = models.TextField(null=True)
    related_controls = models.TextField(null=True)
    applicable_systems = models.TextField(null=True)

class Company_Profile(models.Model):
    name = models.CharField(max_length=130)
    systems = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    certification_requirements = ArrayField(models.CharField(max_length=200), null=True, blank=True)