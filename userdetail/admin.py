from django.contrib import admin

from .models import UserDetails


class UserDetailsAdmin(admin.ModelAdmin):
    # 要列出的字段
    list_display = ('id', 'website', 'company', 'balance', 'add_time',)
    # 可以搜索的字段
    search_fields = ('user', 'bio')
    # 列出可以编辑的字段
    list_editable = ('balance',)
    # 根据某个字段排序
    ordering = ('id',)
    # 分页，每页显示多少条
    list_per_page = 30


admin.site.register(UserDetails, UserDetailsAdmin)

