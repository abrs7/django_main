from django import forms
from django.core import validators
# from first_app import User
from first_app.models import User

class NewUser(forms.ModelForm):
    class Meta():
        model = User
<<<<<<< HEAD
        fields = '__all__'





=======
        fields = '__all__'
>>>>>>> 0d27c795c3a64587703131ed0e3c318222288932
