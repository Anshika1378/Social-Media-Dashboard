from django import forms
from django.contrib.auth.hashers import check_password
from .models import UserRegistration_model,Post


class User_Registration_Form(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email id'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserRegistration_model.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exist')
        return email
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) <= 6:
            raise forms.ValidationError('Password must be atleast unique character and atleat 6')
        return password
    

class Login_Form(forms.Form):
    account = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter your email/username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'Enter your Password'
    }))    

    
# postform
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }