
from django.contrib import admin
from django.urls import path

from sorobanapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", views.index, name = 'index'),
    path("mitorizan",views.mitorizan, name = 'mitorizan'),
    path("kakezan",views.kakezan, name= 'kakezan'),
    path("warizan",views.warizan, name= 'warizan'),
    path("contact",views.contact, name= 'contact'),
    path("contact/complete",views.complete, name= 'complete'),

]
