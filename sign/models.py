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

