from rest_framework import serializers
from .models import course_names, contact_form, enroll_form

class CourseNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_names
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_form
        fields = '__all__'
    
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be a valid domain (e.g., @example.com).")
        return value

    def validate_message(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value

class EnrollFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = enroll_form
        fields = '__all__'
    
    def validate_phonenumber(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits long.")
        return value
    
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be a valid domain (e.g., @example.com).")
        return value 
    
    def validate(self, data):
        email = data.get('email')
        course = data.get('course')
        if not email or not course:
            raise serializers.ValidationError("Email and Course are required fields.")
        return data
