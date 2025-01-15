"""
URL configuration for erp_db project.

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
from .views import UserLoginView, UserRegistrationView , view_all_users 

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('view', view_all_users, name='view_users'),
    # path('update_user/<int:user_id>/', update_user, name='update_user'),
    # path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]


# {
#     "email": "testuser@example.com",
#     "username": "testuser",
#     "password": "securepassword123",
#     "user_type": "student",
#     "fullname": "Test User",
#     "qualification": "B.Tech",
#     "passing_year": 2025,
#     "address": "123 Test Street"
# }
