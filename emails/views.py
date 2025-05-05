from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from . import models
from . import services
# Create your views here.
def email_validation_view(request):
    if request.method == 'POST':
        form = forms.EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            services.email_verification_event(email)

        else:
            print(form.errors)
    else:
        form = forms.EmailForm()

    return render(request,'home.html',{'form':form})


def verifey_email_token_view(request,token):
    did_verifey,msg = services.verifey_token(token)

    if not did_verifey:
        return HttpResponse(msg)
    return HttpResponse(token)
