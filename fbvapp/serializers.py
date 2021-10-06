from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from fbvapp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','score']