from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control", "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))



class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control", "pattern": "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))