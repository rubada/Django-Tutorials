from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm,
    CustomUserUpdateForm,
    )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_update(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # redirect to wherever you want to land after saving
            return redirect('profile_update')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, "accounts/profile_update.html", {"form": form})
