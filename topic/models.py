from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TopicCategory(models.Model):
    """
    话题标签表
    """
    CATEGORY_TYPE = (
        (1, "tab"),
        (2, "go"),
    )

    name = models.CharField(default='', max_length=30, verbose_name='类别名', help_text='类别名')
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    header_color = models.CharField(default="#001D25", max_length=30, verbose_name="头部颜色",
                                    help_text="头部颜色")
    desc = models.TextField(null=True, blank=True, verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="node 类型", help_text="node 类型")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_hot = models.BooleanField(default=False, verbose_name="是否最热", help_text="是否最热")
    avatar = models.CharField(max_length=50, null=True, blank=True, default="/static/img/default-avatar.png",
                              verbose_name="头像")
    background_img = models.CharField(max_length=50, null=True, blank=True, default="/static/img/default-avatar.png",
                                      verbose_name="背景图片")
    theme_color = models.CharField(default="#001D25", max_length=30, verbose_name="主题颜色",
                                   help_text="主题颜色")
    count_topic = models.IntegerField(default=0, verbose_name="统计此节点下一共有多少个Topic")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name
        unique_together = ('code', 'category_type',)

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    话题表
    """
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(TopicCategory, verbose_name='分类', on_delete=models.CASCADE)

    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='标题')
    content = models.TextField(max_length=20000, blank=True, verbose_name='内容')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    comment_num = models.IntegerField(default=0, verbose_name='评论数量')
    last_comment_user = models.CharField(max_length=50, null=True, blank=True, default='', verbose_name='最后评论人')
    last_comment_time = models.DateTimeField(null=True, blank=True, verbose_name='最后评论时间')

    click_num = models.IntegerField(default=0, verbose_name='点击数量')

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NodeLink(models.Model):
    """
    话题节点表
    """
    pass


class Comment(models.Model):
    """
    评论表
    """
    topic = models.ForeignKey(Topic, verbose_name='话题', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='评论者', on_delete=models.CASCADE)
    content = models.TextField(max_length=20000, null=True, blank=True, verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content






