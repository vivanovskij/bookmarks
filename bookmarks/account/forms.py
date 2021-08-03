from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, help_text="Это подсказка")
    password = forms.CharField(widget=forms.PasswordInput)
