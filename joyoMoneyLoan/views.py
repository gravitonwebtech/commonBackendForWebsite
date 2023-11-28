

# Create your views here.
# views.py
from rest_framework import generics
from .models import NormalData
from .serializers import NormalDataSerializer
from .models import Email, Image, Register
from .serializers import EmailSerializer, ImageSerializer, RegisterSerializer
class NormalDataView(generics.ListCreateAPIView):
    queryset = NormalData.objects.all()
    serializer_class = NormalDataSerializer

from .models import LoanApplication, Email, Image, Register
from .serializers import LoanApplicationSerializer, EmailSerializer, ImageSerializer, RegisterSerializer

class LoanApplicationView(generics.CreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

class LoanApplicationByEmailView(generics.RetrieveAPIView):
    serializer_class = LoanApplicationSerializer
    lookup_field = 'email'

    def get_queryset(self):
        email = self.kwargs['email']
        return LoanApplication.objects.filter(email=email)

class EmailView(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)

        if email and password:
            return Register.objects.filter(email=email, password=password)
        return Register.objects.none()