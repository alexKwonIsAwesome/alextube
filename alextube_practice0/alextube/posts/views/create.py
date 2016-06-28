from django.views.generic import View
from django.shortcuts import render


class PostCreateView(View):
    

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "posts/new.html",
                context={},
        )
