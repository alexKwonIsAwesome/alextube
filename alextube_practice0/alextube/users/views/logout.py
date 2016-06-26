from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
                request,
                messages.SUCCESS,
                "You are successfully logged out. Thanks for using and hope to see you again."
        )
        return redirect(reverse("login"))
