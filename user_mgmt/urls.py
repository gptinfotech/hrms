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
from .views import UserListCreateAPIView, UserDetailAPIView, UserTypeListCreateAPIView, UserTypeDetailAPIView
from .views import SystemModuleListCreateAPIView, SystemModuleDetailAPIView, UserTypeModuleMappingListCreateAPIView, UserTypeModuleMappingDetailAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:user_id>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('usertypes/', UserTypeListCreateAPIView.as_view(), name='user-type-list-create'),
    path('usertypes/<int:user_type_id>/', UserTypeDetailAPIView.as_view(), name='user-type-detail'),
    path('systemmodules/', SystemModuleListCreateAPIView.as_view(), name='system-module-list-create'),
    path('systemmodules/<int:system_module_id>/', SystemModuleDetailAPIView.as_view(), name='system-module-detail'),
    path('usertype-module-mappings/', UserTypeModuleMappingListCreateAPIView.as_view(), name='user-type-module-mapping-list-create'),
    path('usertype-module-mappings/<int:mapping_id>/', UserTypeModuleMappingDetailAPIView.as_view(), name='user-type-module-mapping-detail'),
]
