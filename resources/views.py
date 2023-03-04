from rest_framework import viewsets, permissions
from .models import Company, CustomUser
from .serializers import CompanySerializer, CustomUserSerializer, LoginSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from requests import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_protect



class CompanyViewSet(viewsets.ModelViewSet):
   queryset = Company.objects.all()
   serializer_class = CompanySerializer
   permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
   queryset = CustomUser.objects.all()
   serializer_class = CustomUserSerializer


   permission_classes = [permissions.IsAuthenticated]


class LoginView(APIView):
   def post(self, request, format=None):
       import pdb; pdb.set_trace()
       serializer = LoginSerializer(data=request.data)
       if serializer.is_valid():
           user = serializer.validated_data['user']
           token, created = Token.objects.get_or_create(user=user)
           return Response({'token': token.key, 'user_id': user.pk,      'email': user.email})
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [permissions.IsAuthenticated]


   def post(self, request, format=None):
       request.user.auth_token.delete()
       return Response(status=status.HTTP_200_OK)

@login_required
def company_detail(request, pk):
   company = get_object_or_404(Company, pk=pk)
   return render(request, 'company_detail.html', {'company': company})


@login_required
def user_detail(request, pk):
   
   user = get_object_or_404(CustomUser, pk=pk)
   return render(request, 'user_detail.html', {'user': user})

def login_page(request):
	return render(request, 'login.html')

def signup_page(request):
    # import pdb; pdb.set_trace()
    return render(request, 'signup.html')

