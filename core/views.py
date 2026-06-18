from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from .models import products
from .forms import loginform, registerform
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin,ListView):
    model=products
    template_name='home.html'
    fields=['name', 'products','price']
    context_object_name='product'
    def get_queryset(self):
        return products.objects.filter(user=self.request.user)
    

class About(LoginRequiredMixin,TemplateView):
    template_name='about.html'

class Detail(LoginRequiredMixin,DetailView):
    model=products
    template_name='individual.html'
    context_object_name='individual'

class Login(View):
    def get(self, request):
        form=loginform
        return render(request, 'login.html', { 'form':form })
    
    def post(self, request):
        data_form=loginform(request.POST)
        if data_form.is_valid():
            username=data_form.cleaned_data['username']
            password=data_form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', { 'user_none': 'incorrect credentials' })
        else:
            return render(request, 'login.html', { 'invalid_input':'invalid input' })
        
class Register(View):
    def get(self, request):
        form=registerform
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=registerform(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']

            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    return render(request, 'register.html', { 'user_err':'user already exists...login' })
                else:
                    user=User.objects.create_user(username=username, password=pass1)
                    login(request, user)
                    return redirect('home')
            else:
                return render(request, 'register.html', { 'pass_err':'enter the same passowords in both the fields' })
                

