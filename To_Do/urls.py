"""
URL configuration for To_Do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from myapp.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,TaskToggleView, RegistrationView, CustomLoginView,CustomLogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('index/', TaskListView.as_view(), name='index'),
    path('new/', TaskCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('toggle/<int:pk>/',TaskToggleView.as_view(),name='toggle')
]
