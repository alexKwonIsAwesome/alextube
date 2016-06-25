from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


class SignupView(View):
    
    def get(self, request, *args, **kwargs):
        return render(
                request,
                "users/signup.html",
                context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        phonenumber = request.POST.get("phonenumber")

        user = get_user_model().objects.create_user(
                username=username,
                password=password,
                phonenumber=phonenumber,
        )

        return redirect(reverse("login"))
