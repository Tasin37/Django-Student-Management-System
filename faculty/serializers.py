from faculty.models import *
from rest_framework import serializers
from faculty.validators import validate_salary


class TeacherSerializer(serializers.ModelSerializer):
    salary = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_salary])
    class Meta:
        model = Teacher
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class DepartmentHeadSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    class Meta:
        model = DepartmentHead
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    teachers = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'

    def validate_name(self,value):
        if Department.objects.filter(name_iexact=value).exists():
            raise serializers.ValidationError("Department with this name already exists.")