from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from user.models import UserProfile


User = get_user_model()


class Topic(models.Model):
    """
    话题表
    """
    pass


class TopicCategory(models.Model):
    """
    话题标签表
    """
    pass


class NodeLink(models.Model):
    """
    话题节点表
    """
    pass


class Comments(models.Model):
    """
    评论表
    """
    pass





