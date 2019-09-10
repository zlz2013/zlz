
from django import forms

class Reg2(forms.Form):
    username=forms.CharField(max_length=30,label='请输入用户名')
    password=forms.CharField(max_length=30,label='请输入密码')
    password2=forms.CharField(max_length=20,label='确认密码')

    def clean_username(self):
        name=self.cleaned_data['username']
        if '*' in name:
            raise forms.ValidationError('用户名不能为空')
        return name

    def clean_password(self):
        pass

