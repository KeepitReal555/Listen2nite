from django.urls import path, include

from .views import (
    CreateTopicView, CreateCommentView,
    TopicListView, TopicDetailView,
)

app_name = 'topic'


urlpatterns = [
    path('', TopicListView.as_view(), name='index'),
    path('topic/', include(([
        path('', TopicListView.as_view, name='topic_list'),
    ]))),
]