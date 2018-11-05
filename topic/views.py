from datetime import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView, CreateView,
    ListView,
)

import markdown

from .models import Topic, TopicCategory, Comment
from .forms import CreateTopicForm, CreateCommentForm


User = get_user_model()


class TopicListView(ListView):
    """
    展示 Topic 列表视图
    """
    model = Topic
    template_name = 'topic/index.html'
    context_object_name = 'topics'
    queryset = Topic.objects.all()
    ordering = ('update_time', )
    paginate_by = 20



class CreateTopicView(CreateView):
    """
    创建 Topic 视图
    """
    model = Topic
    form_class = CreateTopicForm

    def form_valid(self, form):
        """
        将 Topic 与作者关联起来
        :param form:
        :return:
        """



class TopicDetailView(DetailView):
    """
    展示 Topic 详情视图
    """
    model = Topic
    template_name = ''

    def get_context_data(self, **kwargs):
        """
        向模板传入 Topic 及其评论上下文.
        :param kwargs:
        :return:
        """

        return super(TopicDetailView, self).get_context_data(**kwargs)


class CreateCommentView(CreateView):
    """
    创建评论视图
    """
    model = Comment
    form_class = CreateCommentForm

    def form_valid(self, form):
        """
        将评论与评论者关联起来
        :param form:
        :return:
        """
        pass


