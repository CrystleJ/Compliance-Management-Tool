# Generated by Django 4.1.4 on 2023-02-21 02:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_cert_req_company_profile_certification_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_profile',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]
