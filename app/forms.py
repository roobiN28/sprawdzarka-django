from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Test, Solution


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('input_data', 'output_data')


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('program_code',)

class LoginForm(forms.Form):
    username = forms.CharField(label="Login:", max_length=30)
    password = forms.CharField(label="Hasło:", widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError("Niepoprawny login")

    def clean_password(self):
        if self.cleaned_data.has_key('username'):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Niepoprawne hasło")
        raise forms.ValidationError("Niepoprawny login")

class RegisterForm(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())
    phone = forms.CharField(label="Telefon:",max_length=20,required=False)
    log_on = forms.BooleanField(label="Logowanie po rejestracji:",required=False)