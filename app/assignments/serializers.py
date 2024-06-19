from rest_framework import serializers
from core.models import Assignment
#always make sure the fields in here match to the fieldnames in corresponding model
class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assignment
        fields=['id','name','sectionID','duedate','filelocation','instructions','subjectID','teacherID','teacherName']
        read_only_fields = ['id']