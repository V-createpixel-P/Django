
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    
] 
#+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)