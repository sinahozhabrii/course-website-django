from django.http import HttpResponse
from django_htmx.http import HttpResponseClientRedirect
from django.shortcuts import redirect, render
from . import forms
from . import models
from . import services
from course import services as course_services
from django.contrib import messages
# Create your views here.

def login_logout_view(request):
    return render(request,'auth/login-logout.html',{})

def logout_view(request):
    if not request.htmx:
        return redirect('/')
    if request.method == 'POST':
        try:
            del request.session['email_id']
            del request.session['next_url']
        except:
            pass
    email_id = request.session.get('email_id')
    if not email_id:
        return HttpResponseClientRedirect("/")
    return render(request,'emails/hx/logout-btn.html')
    
def email_validation_view(request):
        if not request.htmx:
            return redirect('/')
        email_id = request.session.get('email_id')
        context = {'form':forms.EmailForm(),
                   'messages' : None,
                   'show_form': not email_id,
                   'request':request,
                   }
        if request.method == 'POST':
            form = forms.EmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                services.email_verification_event(email)
                context['messages'] = f'email succesfully send pls check your email'
            else:
                print(form.errors)
        
        return render(request,'emails/hx/form.html',context)


def verifey_email_token_view(request,token):
    did_verifey,msg,email_id = services.verifey_token(token)

    if not did_verifey:
        try:
            del request.session['email_id']
            del request.session['next_url']
        except:
            pass
        return HttpResponse(msg)
    
    request.session['email_id'] = f"{email_id}"
    next_url = request.session.get('next_url','/')

    return redirect(next_url)

def home_view(request):
    course_list,subjects = course_services.get_course_list()
    return render(request,'home.html',{'courses':course_list,'subjects':subjects})
