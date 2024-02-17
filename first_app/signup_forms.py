from django import forms
from django.core import validators
# from first_app import User
from first_app.models import User

class NewUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'





