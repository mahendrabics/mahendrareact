# Generated by Django 4.1.7 on 2023-03-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0006_rename_projectid_project_projectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinvoices',
            name='InvoiceNo',
            field=models.CharField(max_length=50),
        ),
    ]