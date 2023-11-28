# serializers.py
from rest_framework import serializers
from .models import *

class NormalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalData
        fields = '__all__'
# serializers.py
from .models import LoanApplication, Email, Image, Register

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'