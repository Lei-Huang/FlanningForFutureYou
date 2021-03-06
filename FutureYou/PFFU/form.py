from django import forms
from captcha.fields import CaptchaField


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    account = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"validate code wrong"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)