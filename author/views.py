from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import  update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from cars.models import Order




class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

    
    
    

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('user_login')