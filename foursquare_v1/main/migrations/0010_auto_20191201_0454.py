# Generated by Django 2.2.7 on 2019-12-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191130_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='customer_company_name_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_facebook',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_fax',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_line',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_linkedin',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_post_code',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_skype',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_tel',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_website',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_wechat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customertable',
            name='customer_whatsapp',
            field=models.TextField(null=True),
        ),
    ]
