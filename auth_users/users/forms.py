from django import forms
from django.contrib.auth import authenticate, get_user_model


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This does not exist!!!")
            if not user.check_password(password):
                raise forms.ValidationError("Your password is not correct!!!")
            if not user.is_active:
                raise forms.ValidationError("This account is not active!!!")
        return super(UserLoginForm, self).clean(*args, **kwargs)


User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label="Firstname")
    last_name = forms.CharField(label="Lastname")
    email = forms.EmailField(label="E-mail Address")
    password1 = forms.CharField(
        widget=forms.PasswordInput, label="New Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username_query = User.objects.filter(username=username)
        if username_query.exists():
            raise forms.ValidationError("This username has already taken!!!")
        email_query = User.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError("This email has already taken!!!")
        if password1 != password2:
            raise forms.ValidationError("Password did not match!!!")
        return super(UserRegistrationForm, self).clean(*args, **kwargs)
