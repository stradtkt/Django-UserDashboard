from django import forms 

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
    confirm_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
