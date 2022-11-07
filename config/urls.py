"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from habit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/logout/',views.logout, name='logout' ),
    path('', views.index, name="home"),
    path('habit/new', views.create_habit, name='create_habit'),
    path('habit/<int:pk>',views.habit_detail, name='habit_detail'),
    path('habit/new/<int:habitpk>', views.edit, name="edit"),
    path('habit/delete/<int:habitpk>', views.habit_delete, name='habit_delete'),
    path('record/new', views.create_record, name="create_record"),
    path('record/<int:pk>/edit/', views.edit_record, name='edit_record'),
    path('accounts/login/', views.login, name="login"),
]
