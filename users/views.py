from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.user.is_authenticated:
        return redirect('listing_list')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"تم إنشاء الحساب بنجاح! مرحباً بك، {user.username}.")
            return redirect('listing_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
