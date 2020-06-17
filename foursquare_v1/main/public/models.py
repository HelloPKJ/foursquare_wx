from django.db import models

# 客户数据表
class CustomerTable(models.Model):

    # 客户ID
    customer_id = models.fields.AutoField(primary_key=True,db_index=True)
    # 客户官网
    customer_website = models.fields.TextField(null=True)
    # 客户邮箱
    customer_email = models.fields.TextField(null=True)
    # 客户所属行业ID
    customer_trades_id = models.fields.PositiveSmallIntegerField(null=True,db_index=True)
    # 客户数据数据来源ID
    customer_data_sources_id = models.fields.PositiveSmallIntegerField(null=True,db_index=True)
    # 客户采购清单CN
    customer_need_product_cn = models.fields.TextField(null=True)
    # 客户采购清单EN
    customer_need_product_en = models.fields.TextField(null=True)
    # 客户所属区域1级CN
    customer_region1_cn = models.fields.CharField(max_length=32,null=True)
    # 客户所属区域1级EN
    customer_region1_en = models.fields.CharField(max_length=32,null=True)
    # 客户所属区域2级CN
    customer_region2_cn = models.fields.CharField(max_length=32,null=True,db_index=True)
    # 客户所属区域2级EN
    customer_region2_en = models.fields.CharField(max_length=32,null=True,db_index=True)
    # 客户公司名称EN
    customer_company_name_en = models.fields.TextField(null=True)
    # 客户公司地址
    customer_adds_en = models.fields.TextField(null=True)
    # 客户地址邮编
    customer_post_code = models.fields.TextField(null=True)
    # 客户联系人
    customer_name = models.fields.TextField(null=True)
    # 客户电话
    customer_tel = models.fields.TextField(null=True)
    # 客户传真
    customer_fax = models.fields.TextField(null=True)
    # 客户图片
    customer_photo = models.FileField(upload_to='customer_photo',null=True)
    # 客户skype
    customer_skype = models.fields.TextField(null=True)
    # 客户whatsapp
    customer_whatsapp = models.fields.TextField(null=True)
    # 客户facebook
    customer_facebook = models.fields.TextField(null=True)
    # 客户微信
    customer_wechat = models.fields.TextField(null=True)
    # 客户Line
    customer_line = models.fields.TextField(null=True)
    # 客户linkedin
    customer_linkedin = models.fields.TextField(null=True)
    # 客户数据状态
    customer_state = models.fields.PositiveSmallIntegerField(default=1)
    # 客户数据是否软删除
    customer_isdel = models.fields.BooleanField(default=False)
    # 客户备注
    customer_explain = models.fields.TextField(null=True)
    # 客户数据注册时间
    customer_regtime = models.fields.DateTimeField(null=True)
    # 客户最后一次修改时间
    custome_last_update_time = models.fields.DateTimeField(null=True)


    class Meta():
        # 设置表名
        db_table = 'customer_table'



# 所属行业表
class TradesTable(models.Model):
    # 所属行业ID
    trades_id  = models.fields.AutoField(primary_key=True, db_index=True)
    # 所属行业名称CN
    trades_name_cn = models.fields.CharField(max_length=32,null=True,db_index=True)
    # 所属行业名称EN
    trades_name_en = models.fields.CharField(max_length=64,null=True,db_index=True)
    # 所属行业数据状态
    trades_state = models.fields.PositiveSmallIntegerField(default=1)
    # 所属行业是否软删除
    trades_isdel = models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'trades_table'



#数据来源表
class DataSourcesTable(models.Model):
    # 数据来源ID
    data_sources_id = models.fields.AutoField(primary_key=True,db_index=True)
    # 数据来源名称CN
    data_sources_name_cn = models.fields.CharField(max_length=32,null=True,db_index=True)
    # 数据来源名称EN
    data_sources_name_en = models.fields.CharField(max_length=64,null=True,db_index=True)
    # 数据来源数据状态
    data_sources_state = models.fields.PositiveSmallIntegerField(default=1)
    # 数据来源是否软删除
    data_sources_isdel =models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'data_sources_table'



#关于我们表
class AboutTable(models.Model):
    # 关于我们ID
    about_id = models.fields.AutoField(primary_key=True)
    # 关于我们logo图片
    about_logo = models.FileField(upload_to='about_img',null=True)
    # 关于我们产品简介
    about_explain = models.fields.TextField(null=True)
    # 关于我们公告
    about_notice = models.fields.TextField(null=True)
    # 关于我们官网
    about_website = models.fields.CharField(max_length=64,null=True)
    # 关于我们联系方式
    about_Contact = models.fields.CharField(max_length=64,null=True)
    # 关于我们二维码图片
    about_qrcode_img = models.FileField(upload_to='about_img',null=True)
    # 关于我们二维码图片说明
    about_qrcode_explain = models.fields.CharField(max_length=64,null=True)
    # 关于我们数据状态
    about_state = models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'about_table'



# 广告表
class AdsTable(models.Model):
    # 广告ID
    ads_id = models.fields.AutoField(primary_key=True,db_index=True)
    # 广告标题
    ads_title = models.fields.CharField(max_length=32,null=True)
    # 广告说明
    ads_explain = models.fields.TextField(null=True)
    # 广告图片
    ads_img = models.FileField(upload_to='ads_img',null=True)
    # 广告跳转链接
    ads_url = models.fields.URLField(null=True)
    # 点击次数
    ads_click_num = models.fields.PositiveIntegerField(default=0)
    # 广告状态
    ads_state = models.fields.PositiveSmallIntegerField(default=1)
    # 广告是否软删除
    ads_isdel = models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'ads_table'



# 评价表
class EvaluationTable(models.Model):
    # 评价ID
    evaluation_id = models.fields.AutoField(primary_key=True,db_index=True)
    # 评价图片
    evaluation_img = models.FileField(upload_to='evaluation_img',null=True)
    # 评价标题
    evaluation_title = models.fields.CharField(max_length=32,null=True)
    # 评价内容
    evaluation_content = models.fields.TextField(null=True)
    # 评价状态
    evaluation_state = models.fields.PositiveSmallIntegerField(default=1)
    # 评价是否软删除
    evaluation_isdel = models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'evaluation_table'



# 热门国家
class HotCountryTable(models.Model):
    # 热门国家ID
    hot_country_id  = models.fields.AutoField(primary_key=True, db_index=True)
    # 热门国籍CN
    hot_country_cn = models.fields.CharField(max_length=64,null=True,db_index=True)
    # 热门国籍状态
    hot_country_state = models.fields.PositiveSmallIntegerField(default=1)
    # 热门国籍是否软删除
    hot_country_isdel = models.fields.BooleanField(default=False)


    class Meta():
        # 设置表名
        db_table = 'hot_country_table'
