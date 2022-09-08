import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Mailme
from .serializers import MailSerializer

class SendMail(viewsets.ModelViewSet):
    queryset = Mailme.objects.all()
    serializer_class = MailSerializer


