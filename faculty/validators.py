from rest_framework import serializers

def validate_salary(value):
    if value < 0:
        raise serializers.ValidationError("Salary must be greater than 0.")
    return value