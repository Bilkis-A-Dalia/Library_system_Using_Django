from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from order.models import Order
from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash,authenticate



@login_required
def profile(request):
    books = Order.objects.filter(user=request.user)
    return render(request,'profile.html',{'books':books})

class RegistrationView(CreateView):
    template_name = 'form.html'
    form_class = forms.RegistrationForm
    
    def get_success_url(self):
        return reverse_lazy('homepage')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Signup'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Account registration done successfully')
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'form.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request,'Login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Login information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='login'
        return context
    
class UserLogoutView(LogoutView):
    def get_success_url(self) :
        return reverse_lazy('homepage')
    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form=forms.ChangeDataForm(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('homepage')       
    else:
        edit_form = forms.ChangeDataForm(instance = request.user)
    return render(request,'form.html',{'form':edit_form,'type':'update'})

@login_required
def order(request,id):
    book = Book.objects.get(pk=id)
    if book.quantity > 0:
        book.quantity -= 1
        messages.success(request,'congratulation for borrow the bokk')
        book.save()
        Order.objects.create(user = request.user,book = book)
    else:
        messages.warning(request,'Book are not available now')
    return redirect('profile')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request, 'form.html', {'form':form,'type': 'Password Change'})
    else:
        return redirect('login')