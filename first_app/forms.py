from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Please make sure your name starts with Z ')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z],max_length=34)
    email = forms.EmailField(max_length=25)
    verify_email = forms.EmailField(max_length=25, label="Please Enter your Email again")
    text = forms.CharField(widget=forms.Textarea)

    
    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        v_mail = all_cleaned_data['verify_email']
        # text = all_cleaned_data['text']
        if email and v_mail and email != v_mail :
            raise forms.ValidationError("Please make sure your email are correct!")
        return all_cleaned_data 


