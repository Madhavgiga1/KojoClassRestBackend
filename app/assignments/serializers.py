from rest_framework import serializers
from core.models import Assignement

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assignement
        fields=['id','name','classID','duedate','fileurl','instructions','subjectID','teacherID','teacherName']
        read_only_fields = ['id']