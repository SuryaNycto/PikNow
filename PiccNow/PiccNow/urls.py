
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('sign-in/',auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/',auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/',views.sign_up),


    path('customer/',views.customerpage,name="customer"),
    path('courier/',views.courierpage,name="courier"),
]
