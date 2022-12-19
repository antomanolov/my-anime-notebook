from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from project_defense.profileapp.forms import UserCreateForm
from project_defense.profileapp.utilities.user_model_for_app import UserModel


class SignUpView(CreateView):
    form_class = UserCreateForm
    template_name = 'profiles/profile_create.html'
    success_url = reverse_lazy('index page')


class SignInView(LoginView):
    template_name = 'profiles/profile_sign_in.html'


class SignOutView(LogoutView):
    pass


class ProfileEdit(UpdateView):
    model = UserModel
    fields = ('first_name', 'last_name', 'profile_picture', 'email')
    template_name = 'profiles/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile details page', kwargs={
            'pk': self.request.user.pk,
        })


class ProfileDetails(DetailView):
    model = UserModel
    template_name = 'profiles/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owned_by'] = self.request.user == self.object
        return context


# TODO make this form only for the user id
class ProfileDelete(DeleteView):
    model = UserModel
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('index page')
