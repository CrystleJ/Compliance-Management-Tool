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
    control_id = models.CharField(max_length=30, primary_key=True)
    family = models.CharField(max_length=100, null=True, blank=True)
    control_txt = models.TextField(null=True, blank=True)
    discussion = models.TextField(null=True, blank=True)

class NIST_172_Controls(models.Model):
    control_id = models.CharField(max_length=30, primary_key=True)
    family = models.CharField(max_length=100, null=True, blank=True)
    control_txt = models.TextField(null=True, blank=True)
    discussion = models.TextField(null=True, blank=True)

class NIST_53_Controls(models.Model):
    control_name = models.CharField(max_length=200)
    control_id = models.CharField(max_length=30, primary_key=True)
    control_txt = models.TextField()
    discussion = models.TextField()
    cmmc_level = models.PositiveIntegerField()
    control_id_171 = models.ForeignKey(NIST_171_Controls, on_delete=models.CASCADE)
    control_id_172 = models.ForeignKey(NIST_172_Controls, on_delete=models.CASCADE)
    related_controls = models.CharField(max_length=200, null=True, blank=True)
    applicable_systems = models.TextField()