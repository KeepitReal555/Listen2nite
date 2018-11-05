from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, FormView
)

from .models import UserDetails
from .forms import SettingsForm


@method_decorator([login_required], name='dispatch')
class SettingsView(FormView):
    """
    更改用户信息的设置视图.
    """
    # model = UserDetails
    form_class = SettingsForm
    template_name = 'userdetail/settings.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        user_detail = UserDetails.objects.filter(user=user).first()
        # print('user_detail', user_detail.company)
        if not user_detail:
            user_detail = UserDetails.objects.create(user=user)
        kwargs['user_detail'] = user_detail
        kwargs['user'] = user

        return super(SettingsView, self).get_context_data(**kwargs)


    def form_valid(self, form):
        # has_error = True
        user = self.request.user
        data = form.cleaned_data
        print(data)
        user_detail_obj = UserDetails.objects.filter(user=user).first()
        user_detail_obj.__dict__.update(data)
        user_detail_obj.save()
        uset_detail = UserDetails()
        # user_detail = form.save(commit=False)
        # user_detail.save()
        # form.save_m2m()
        return redirect('userdetail:settings')

