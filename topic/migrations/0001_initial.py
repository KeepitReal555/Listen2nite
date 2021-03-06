# Generated by Django 2.1.2 on 2018-11-05 04:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=20000, null=True, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 11, 5, 12, 6, 16, 363520), verbose_name='添加时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
            },
        ),
        migrations.CreateModel(
            name='NodeLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(blank=True, max_length=20000, verbose_name='内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 11, 5, 12, 6, 16, 362506), verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论数量')),
                ('last_comment_user', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='最后评论人')),
                ('last_comment_time', models.DateTimeField(blank=True, null=True, verbose_name='最后评论时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '话题表',
                'verbose_name_plural': '话题表',
            },
        ),
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('header_color', models.CharField(default='#001D25', help_text='头部颜色', max_length=30, verbose_name='头部颜色')),
                ('desc', models.TextField(blank=True, help_text='类别描述', null=True, verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, 'tab'), (2, 'go')], help_text='node 类型', verbose_name='node 类型')),
                ('is_hot', models.BooleanField(default=False, help_text='是否最热', verbose_name='是否最热')),
                ('avatar', models.CharField(blank=True, default='/static/img/default-avatar.png', max_length=50, null=True, verbose_name='头像')),
                ('background_img', models.CharField(blank=True, default='/static/img/default-avatar.png', max_length=50, null=True, verbose_name='背景图片')),
                ('theme_color', models.CharField(default='#001D25', help_text='主题颜色', max_length=30, verbose_name='主题颜色')),
                ('count_topic', models.IntegerField(default=0, verbose_name='统计此节点下一共有多少个Topic')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 11, 5, 12, 6, 16, 361862), verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='topic.TopicCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': 'Topic类别',
                'verbose_name_plural': 'Topic类别',
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.TopicCategory', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic', verbose_name='话题'),
        ),
        migrations.AlterUniqueTogether(
            name='topiccategory',
            unique_together={('code', 'category_type')},
        ),
    ]
