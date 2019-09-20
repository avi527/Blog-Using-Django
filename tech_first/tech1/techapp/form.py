from django import forms
from .models import Register,Imageupload,Addpost
class Signupfrom(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
class Uploadimage(forms.ModelForm):
    class Meta:
        model=Imageupload
        fields = '__all__'

class Postadd(forms.ModelForm):
    class Meta:
        model=Addpost
        fields='__all__'
