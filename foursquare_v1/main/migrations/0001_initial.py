# Generated by Django 2.2.7 on 2019-11-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTable',
            fields=[
                ('about_id', models.AutoField(primary_key=True, serialize=False)),
                ('about_logo', models.FileField(null=True, upload_to='about_img')),
                ('about_explain', models.TextField(null=True)),
                ('about_notice', models.TextField(null=True)),
                ('about_website', models.CharField(max_length=64, null=True)),
                ('about_Contact', models.CharField(max_length=64, null=True)),
                ('about_qrcode_img', models.FileField(null=True, upload_to='about_img')),
                ('about_qrcode_explain', models.CharField(max_length=64, null=True)),
                ('about_state', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'about_table',
            },
        ),
        migrations.CreateModel(
            name='AdsTable',
            fields=[
                ('ads_id', models.AutoField(primary_key=True, serialize=False)),
                ('ads_title', models.CharField(max_length=32, null=True)),
                ('ads_explain', models.TextField(null=True)),
                ('ads_img', models.FileField(null=True, upload_to='ads_img')),
                ('ads_url', models.URLField(null=True)),
                ('ads_click_num', models.PositiveIntegerField(default=1)),
                ('ads_state', models.PositiveSmallIntegerField(default=1)),
                ('ads_isdel', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ads_table',
            },
        ),
        migrations.CreateModel(
            name='CustomerTable',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_website', models.CharField(max_length=32, null=True)),
                ('customer_email', models.CharField(max_length=32, null=True)),
                ('customer_trades_id', models.PositiveSmallIntegerField(null=True)),
                ('customer_data_sources_id', models.PositiveSmallIntegerField(null=True)),
                ('customer_need_product_cn', models.TextField(null=True)),
                ('customer_need_product_en', models.TextField(null=True)),
                ('customer_region1_cn', models.CharField(max_length=32, null=True)),
                ('customer_region1_en', models.CharField(max_length=32, null=True)),
                ('customer_region2_cn', models.CharField(max_length=32, null=True)),
                ('customer_region2_en', models.CharField(max_length=32, null=True)),
                ('customer_company_name_en', models.CharField(max_length=64, null=True)),
                ('customer_adds_en', models.TextField(null=True)),
                ('customer_post_code', models.CharField(max_length=32, null=True)),
                ('customer_name', models.CharField(max_length=32, null=True)),
                ('customer_tel', models.CharField(max_length=32, null=True)),
                ('customer_fax', models.CharField(max_length=32, null=True)),
                ('customer_photo', models.FileField(null=True, upload_to='customer_photo')),
                ('customer_skype', models.CharField(max_length=32, null=True)),
                ('customer_whatsapp', models.CharField(max_length=32, null=True)),
                ('customer_facebook', models.CharField(max_length=32, null=True)),
                ('customer_wechat', models.CharField(max_length=32, null=True)),
                ('customer_line', models.CharField(max_length=32, null=True)),
                ('customer_linkedin', models.CharField(max_length=32, null=True)),
                ('customer_state', models.PositiveSmallIntegerField(default=1)),
                ('customer_isdel', models.BooleanField(default=False)),
                ('customer_explain', models.TextField(null=True)),
                ('customer_regtime', models.DateTimeField(null=True)),
                ('custome_last_update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'customer_table',
            },
        ),
        migrations.CreateModel(
            name='DataSourcesTable',
            fields=[
                ('data_sources_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_sources_name_cn', models.CharField(max_length=32, null=True)),
                ('data_sources_name_en', models.CharField(max_length=64, null=True)),
                ('data_sources_state', models.PositiveSmallIntegerField(default=1)),
                ('data_sources_isdel', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'data_sources_table',
            },
        ),
        migrations.CreateModel(
            name='EvaluationTable',
            fields=[
                ('evaluation_id', models.AutoField(primary_key=True, serialize=False)),
                ('evaluation_img', models.FileField(null=True, upload_to='evaluation_img')),
                ('evaluation_title', models.CharField(max_length=32, null=True)),
                ('evaluation_content', models.TextField(null=True)),
                ('evaluation_state', models.PositiveSmallIntegerField(default=1)),
                ('evaluation_isdel', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'evaluation_table',
            },
        ),
        migrations.CreateModel(
            name='TradesTable',
            fields=[
                ('trades_id', models.AutoField(primary_key=True, serialize=False)),
                ('trades_name_cn', models.CharField(max_length=32, null=True)),
                ('trades_name_en', models.CharField(max_length=64, null=True)),
                ('trades_state', models.PositiveSmallIntegerField(default=1)),
                ('trades_isdel', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'trades_table',
            },
        ),
    ]
