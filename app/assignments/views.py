from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from assignments import serializers
from core.models import Assignment

# Create your views here. and make small 
class GetAssignmentsViewSet(viewsets.ModelViewSet):

    serializer_class=serializers.AssignmentSerializer
    queryset=Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    