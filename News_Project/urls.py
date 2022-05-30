"""News_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.global_settings import STATIC_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from News_App import views
from django.contrib.auth import views as auth_views
from News_App.views import account_verify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home_View/', views.Home_View.as_view(), name="Home_View"),
    path('Apple_View/', views.Apple_View.as_view(), name="Apple_View"),
    path('Tesla_View/', views.Tesla_View.as_view(), name="Tesla_View"),
    path('World_News_View/', views.World_News_View.as_view(), name="World_News_View"),
    path('Tech_Crunch_View/', views.Tech_Crunch_View.as_view(), name="Tech_Crunch_View"),
    path('Latest_News_View/', views.Latest_News_View.as_view(), name="Latest_News_View"),
    path('India_News_View/', views.India_News_View.as_view(), name="India_News_View"),
    path('India_Business_View/', views.India_Business_View.as_view(), name="India_Business_View"),
    path('India_Health_View/', views.India_Health_View.as_view(), name="India_Health_View"),
    path('India_Science_View/', views.India_Science_View.as_view(), name="India_Science_View"),
    path('India_Sports_View/', views.India_Sports_View.as_view(), name="India_Sports_View"),
    path('India_Technology_View/', views.India_Technology_View.as_view(), name="India_Technology_View"),
    path('India_Entertainment_View/', views.India_Entertainment_View.as_view(), name="India_Entertainment_View"),
    path('Argentina_View/', views.Argentina_View.as_view(), name="Argentina_View"),
    path('Australia_View/', views.Australia_View.as_view(), name="Australia_View"),
    path('Austria_View/', views.Austria_View.as_view(), name="Austria_View"),
    path('Belgium_View/', views.Belgium_View.as_view(), name="Belgium_View"),
    path('Brazil_View/', views.Brazil_View.as_view(), name="Brazil_View"),
    path('Bulgaria_View/', views.Bulgaria_View.as_view(), name="Bulgaria_View"),
    path('Canada_View/', views.Canada_View.as_view(), name="Canada_View"),
    path('China_View/', views.China_View.as_view(), name="China_View"),
    path('Colombia_View/', views.Colombia_View.as_view(), name="Colombia_View"),
    path('Cuba_View/', views.Cuba_View.as_view(), name="Cuba_View"),
    path('Czech_Republic_View/', views.Czech_Republic_View.as_view(), name="Czech_Republic_View"),
    path('Egypt_View/', views.Egypt_View.as_view(), name="Egypt_View"),
    path('France_View/', views.France_View.as_view(), name="France_View"),
    path('Germany_View/', views.Germany_View.as_view(), name="Germany_View"),
    path('Greece_View/', views.Greece_View.as_view(), name="Greece_View"),
    path('Hong_Kong_View/', views.Hong_Kong_View.as_view(), name="Hong_Kong_View"),
    path('Hungary_View/', views.Hungary_View.as_view(), name="Hungary_View"),
    path('Indonesia_View/', views.Indonesia_View.as_view(), name="Indonesia_View"),
    path('Ireland_View/', views.Ireland_View.as_view(), name="Ireland_View"),
    path('Israel_View/', views.Israel_View.as_view(), name="Israel_View"),
    path('Italy_View/', views.Italy_View.as_view(), name="Italy_View"),
    path('Japan_View/', views.Japan_View.as_view(), name="Japan_View"),
    path('Latvia_View/', views.Latvia_View.as_view(), name="Latvia_View"),
    path('Malaysia_View/', views.Malaysia_View.as_view(), name="Malaysia_View"),
    path('Mexico_View/', views.Mexico_View.as_view(), name="Mexico_View"),
    path('Morocco_View/', views.Morocco_View.as_view(), name="Morocco_View"),
    path('Netherland_View/', views.Netherland_View.as_view(), name="Netherland_View"),
    path('New_Zealand_View/', views.New_Zealand_View.as_view(), name="New_Zealand_View"),

    path('Login_View/', views.Login_View.as_view(), name="Login_View"),
    path('', views.Registration_View.as_view(), name="Registration_View"),
    path('Logout_View/', views.Logout_View.as_view(), name="Logout_View"),
    #path(r'ckeditor', include('ckeditor_uploader.urls')),
    path('account-verify/<slug:token>', account_verify, name="account_verify"),
    path('accounts/', include('allauth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)