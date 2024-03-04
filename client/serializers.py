from dataclasses import field
from rest_framework import serializers
from .models import Employee,Team,EmployeeProfile
from django.core.mail import send_mail

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ('is_superuser', 'is_staff', 'groups', 'user_permissions')
        extra_kwargs = {
            "password": {'write_only': True}
        }


    def create(self, validated_data):
        password = validated_data.pop("password")
        instance =  super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance

                
class EmployeeProfileSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    team = serializers.CharField(source='team.team_name')
    class Meta:
        model = EmployeeProfile
        fields = '__all__'
    
    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee =  self.fields.get('employee').create(employee_data)
        validated_data['employee'] = employee
        team_name = validated_data.pop('team')
        team, created = Team.objects.get_or_create(team_name=team_name)
        validated_data['team'] = team
        profile = super().create(validated_data)
        send_mail(
            subject='Confirmation Email',
            message='The details have been added successfully.',
            from_email='sruthikrishnan152@gmail.com',  
            recipient_list=[employee_data.get("email", "")]
            )
        return profile
    
    
    def update(self, instance, validate_data):
        employee_data = validate_data.pop('employee', None)
        if employee_data and instance.employee:
            self.fields.get('employee').update(instance.employee, employee_data)
        team = validate_data.pop('team', None)
        if team:
            instance.team.team_name=team
            instance.team.save()
        return super().update(instance, validate_data)