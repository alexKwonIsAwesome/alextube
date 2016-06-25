from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

class LoginView(View):
    
    def get(self, requests, *args, **kwargs):
        return render(
                requests,
                "users/login.html",
                context={},
        )
        
    def post(self, requests, *args, **kwargs):
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        user = authenticate(
                username="username",
                password="password",
        )

        if user:
            login(request, user)

        return redirect(reverse("login"))
