from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
from . import forms
from . import signup_forms

# Create your views here.


def index(request):
    insert_me={'person': 'Lorem Ipsum Lorem Ipsum ' }
    return render(request,'index.html', context=insert_me)

def begnn(request):
    return HttpResponse('<p>Simpler One</p>')

def users(request):
    user_list = User.objects.order_by('first_name')
    users = {'users': user_list}
    return render(request,'users.html', context= users)

def form_name_view(request):

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Successful!!')
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])
        else:
            return render(request, 'forms.html', {'form': form})

    form = forms.FormName()
    return render(request, 'forms.html', {'form':form})
def others(request):
    contento={'text':'Hello to ur site Everyone!!!', 'number':56}
    return render(request,'others.html', context=contento)
def relative_temp(request):
    return render(request, 'relative_temp.html' )
def signup_form(request):
    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Successful!!')
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])
        else:
            return render(request, 'signup.html', {'form': form})

    form = forms.FormName()
    
    return render(request, 'signup.html',{'form': form})    

