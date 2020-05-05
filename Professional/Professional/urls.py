"""Professional URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Booking import views
from Booking.views import GeneratePDF
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start,name=''),
    path('login/',views.u_login,name='login'),
    path('proceed/',views.save,name='proceed'),
    path('search',views.search,name='search'),
    path('login/book/',views.br,name='book'),
    path('login/cont/',views.cont,name='cont'),
    path('logout/',views.user_logout,name='user_logout'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('reg_page/',views.reg_page,name='reg_page'),
    path('pod/',views.pod,name='all_pod'),
    path('pod_pg/',views.pod_pg,name='pod_pg'),
    path('login/alog/pdf/' , GeneratePDF.as_view()),
    path('receipt/<str:id>/' , GeneratePDF.as_view()),
]
