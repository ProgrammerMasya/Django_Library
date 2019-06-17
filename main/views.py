from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserForm


class UserListView(TemplateView):

    template_name = 'home.html'
    model = User

    def get(self, request, *args, **kwargs):
        args = {
            'users': self.model.objects.all(),
            'user_form': UserForm(),
        }
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
        args = {
            'users': self.model.objects.all(),
            'user_form': form,
        }
        return render(request, self.template_name, args)