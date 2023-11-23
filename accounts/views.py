from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import UpdateView
from .models import User
from .forms import SignupForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class SignupView(View):
    
    def get(self, request):
        form = SignupForm()
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)
    
    def post(self, request):
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        context = {
            'form': form
        }
        
        return redirect("accounts:login")


class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, 'user/profile.html', context)

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy("news:home")
    
    def func(self):
        new = self.get_object()
        if self.request.user == new.user or self.request.user.is_superuser:
            return True
        return False

            
        
        