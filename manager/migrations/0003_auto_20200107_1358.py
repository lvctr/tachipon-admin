# Generated by Django 2.2 on 2020-01-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='situation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
