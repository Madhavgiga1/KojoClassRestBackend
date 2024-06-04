from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from assignments import serializers
from core.models import Assignments

# Create your views here.
class GetAssignmentsViewSet(viewsets.modelviewset):
    
    serializer=serializers.AssignmentSerializer
    queryset=Assignments.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    