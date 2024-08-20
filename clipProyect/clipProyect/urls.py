"""
URL configuration for clipProyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from gastosCompartidos import views

urlpatterns = [
    path('', views.hola, name='hola'),
    path('admin/', admin.site.urls),
    path('hola/', views.hola, name='hola'),
    path('newGasto/<int:monto>/', views.newGasto, name='newGasto'),
    path('newPago/<str:envia>/<str:recibe>/<int:monto>/', views.newPago, name='newPago'),
    path('addPersona/<str:nombre>/', views.addPersona, name='addPersona'),

]
