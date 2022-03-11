
# backend/urls.py

from django.contrib import admin
from django.urls import path, include, re_path  # add this
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from rest_framework import routers                    # add this
from todo import views                            # add this
        
router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this
        
urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls))  ,              # add this
    re_path(r"^", ensure_csrf_cookie(TemplateView.as_view(template_name="index.html"))),

]