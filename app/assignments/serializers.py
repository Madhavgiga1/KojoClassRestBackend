from rest_framework import serializers
from core.models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assignment
        fields=['id','name','classID','duedate','fileurl','instructions','subjectID','teacherID','teacherName']
        read_only_fields = ['id']