# Generated by Django 4.1.6 on 2023-02-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0002_alter_company_gstnumber_alter_company_lutnumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectmilestone',
            name='Milestoneid',
        ),
        migrations.RemoveField(
            model_name='projectpayments',
            name='id',
        ),
        migrations.AlterField(
            model_name='bank',
            name='CompanyID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='ClientId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyLogo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='CompanyID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectpayments',
            name='milestoneid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]