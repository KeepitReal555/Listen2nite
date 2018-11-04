from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class SettingsForm(forms.Form):
    website = forms.CharField(required=False, max_length=50, error_messages={'max_length': '最多50位'})
    company = forms.CharField(required=False, max_length=50, error_messages={'max_length': '最多50位'})
    company_title = forms.CharField(required=False, max_length=50, error_messages={'max_length': '最多50位'})
    location = forms.CharField(required=False, max_length=11, error_messages={'max_length': '最多11位'})
    bio = forms.CharField(required=False, max_length=50, error_messages={'max_length': '最多50位'})
    list_rich = forms.CharField(required=False, max_length=2, error_messages={'max_length': '最多2位'})
    show_balance = forms.CharField(required=False, max_length=2, error_messages={'max_length': '最多2位'})
    my_home = forms.CharField(required=False, max_length=50, error_messages={'max_length': '最多50位'})