# Generated by Django 2.2.7 on 2019-11-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191130_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='customer_fax',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_tel',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
