from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


from .models import TopicCategory, Topic, Comment


User = get_user_model()


# def topic_node_code_validate(topic_node_code):
#     if not TopicCategory.objects.filter(code=topic_node_code, category_type=2).first():
#         raise ValidationError('标签不存在')


class CreateTopicForm(forms.ModelForm):
    """
    创建新 Topic 表单
    """
    title = forms.CharField(max_length=120, required=True,
                            error_messages={'required': '标题不能为空',
                                            'max_length': '字数超过限制'})
    content = forms.CharField(max_length=20000, required=False,
                              error_messages={'max_length': '字数超过限制'})
    category_name = forms.CharField(required=True,
                               error_messages={'required': '标签不能为空'})

    class Meta:
        model = Topic
        fields = ['title', 'content', 'category_name']


class CreateCommentForm(forms.ModelForm):
    """
    创建评论表单
    """
    content = forms.CharField(max_length=20000, required=False,
                              error_messages={'max_length': '字数超过限制'})

    class Meta:
        model = Comment
        fields = ['content']


