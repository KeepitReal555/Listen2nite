from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserDetails(models.Model):
    """
    用户详情表
    """
    CHOICES_TYPE = (
        (0, "不展示"),
        (1, "展示")
    )

    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    website = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="个人网站")
    company = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="所在公司")
    company_title = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="工作职位")
    bio = models.CharField(max_length=300, null=True, blank=True, default="", verbose_name="个人简介")
    balance = models.IntegerField(default=500, verbose_name="财富值，默认500")
    show_balance = models.IntegerField(choices=CHOICES_TYPE, default=1, verbose_name="是否显示余额")
    list_rich = models.IntegerField(choices=CHOICES_TYPE, default=1, verbose_name="是否参与财富榜")
    my_home = models.CharField(max_length=30, null=True, blank=True, default="", verbose_name="登录后首页跳转")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "用户详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


