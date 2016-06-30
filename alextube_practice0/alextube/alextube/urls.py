from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include("users.urls", namespace="users")),

    url(r'^posts/', include("posts.urls", namespace="posts")),
]
