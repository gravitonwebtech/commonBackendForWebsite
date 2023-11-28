"""
URL configuration for commonBackendForWebsite project.

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

from .views import *
urlpatterns = [
      path('api/normalData/', NormalDataView.as_view(), name='normal_data_api'),
     path('api/formLoan/', LoanApplicationView.as_view(), name='loan_application_api'),
    path('api/applyLoanDatabyEmail/<str:email>/', LoanApplicationByEmailView.as_view(), name='loan_application_by_email_api'),
    path('api/email/', EmailView.as_view(), name='email_api'),
    path('api/popupImage/', ImageView.as_view(), name='image_api'),
    path('api/register/', RegisterView.as_view(), name='register_api'),
    path('api/login/', LoginView.as_view(), name='login_api'),

]
