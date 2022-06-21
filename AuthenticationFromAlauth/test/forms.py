from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUserModel


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # for fieldname, field in self.fields.items():
        #     field.widget.attrs.update({
        #         'class': 'form-control'
        #     })

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['remember'] = forms.BooleanField(label='Remember me?', widget=forms.CheckboxInput(attrs={
            'class': 'form-check'
        }), required=False)
