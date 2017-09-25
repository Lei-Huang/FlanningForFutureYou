from rest_framework import serializers
from student.models import Student, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ('id', 'studentId', 'description', 'residentStatus', 'name', 'graduation_year', 'owner')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('studentId', instance.title)
        instance.code = validated_data.get('description', instance.code)
        instance.linenos = validated_data.get('residentStatus', instance.linenos)
        instance.language = validated_data.get('name', instance.language)
        instance.style = validated_data.get('graduation_year', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'student')