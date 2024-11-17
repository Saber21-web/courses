from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .models import UserProfile, Course, Purchase
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:user_cart')
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('users:user_cart')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def user_cart(request):
    user = request.user
    enrolled_courses = Course.objects.filter(students=user)

    return render(request, 'users/users_cart.html', {
        'user': user,
        'enrolled_courses': enrolled_courses
    })
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    user = request.user
    purchases = Purchase.objects.filter(user=user)
    return render(request, 'users/profile.html', {'user': user, 'purchases': purchases})
