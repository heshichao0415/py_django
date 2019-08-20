from django.db import models

# Create your models here.

#基本信息数据统计表
class Basic(models.Model):
    start_time = models.DateTimeField()        #测试开始时间,前端显示需要修改django配置文件
    end_time = models.DateTimeField()          #测试结束时间
    run_time = models.IntegerField()           #测试时间
    sum_case = models.IntegerField()           #用例数
    run_case = models.IntegerField()           #执行用例数
    skip_case = models.IntegerField()          #跳过用例数
"""
前端显示配置文件路径：Python目录/site-packages/django/conf/locale/zh_Hans/formats.py
"""
#测试数据统计
class Statistics(models.Model):
    success_cases = models.IntegerField()         #成功用例数
    fail_cases = models.IntegerField()            #失败用例数
    error_cases = models.IntegerField()           #错误用例数
    skip_cases = models.IntegerField()            #跳过用例数

#详细数据统计
class Detail(models.Model):
    name = models.CharField(max_length=100)           #项目名称
    case_number = models.CharField(max_length=200)       #用例编号
    case_name = models.CharField(max_length=200)         #用例名称
    aip_address = models.CharField(max_length=200)       #接口地址
    aip_method = models.CharField(max_length=100)        #接口方法
    test_result = models.BooleanField()                 #测试结果
    case_detail = models.CharField(max_length=100)      #详细情况

class testdetails(models.Model):
    id1 = models.ForeignKey(Detail)
    name = models.CharField(max_length=300)
    case_name = models.CharField(max_length=300)
    api_address = models.CharField(max_length=200)
    api_method = models.CharField(max_length=200)
    case_data = models.CharField(max_length=200)
    result_data = models.CharField(max_length=300)
    test_result = models.BooleanField()
