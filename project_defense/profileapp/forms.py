from django.contrib.auth import forms as auth_forms
from project_defense.profileapp.utilities.user_model_for_app import UserModel


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {"username": auth_forms.UsernameField}
