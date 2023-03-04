from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('users', views.CustomUserViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   path('company/<int:pk>/', views.company_detail, name='company_detail'),
   path('user/<int:pk>/', views.user_detail, name='user_detail'),
   path('login/', views.LoginView.as_view(), name='login'),
   path('login_page/', views.login_page, name='login_page'),
   path('signup_page/', views.signup_page, name='signup_page')
]
