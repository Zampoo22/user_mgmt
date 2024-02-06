from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, EmployeeProfile

from .serializers import EmployeeSerializer, EmployeeProfileSerializer

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer 
    permission_classes = []
    authentication_classes = []
    
#****json code******
# class EmployeeAPIView(viewsets.ViewSet):
    
#     def create(self, request):
#         data = request.data 
#         employee_data = data.pop("employee_details")
#         try:
#             employee = Employee.objects.create(**employee_data)
#         except: 
#             return Response('email already used',status=status.HTTP_400_BAD_REQUEST)
        
#         team_name = data.pop("team_name")
#         team, created = Team.objects.get_or_create(team_name=team_name)
#         employee_profile = EmployeeProfile.objects.create(**data, employee=employee, team=team)
        
#         send_mail(
#         subject = 'Confirmation Email',
#         message = 'The details have been added successfully.',
#         from_email = 'sruthikrishnan152@gmail.com',  
#         recipient_list = [employee_data.get("email", "")])
#         data = EmployeeProfile.objects.filter(id=employee_profile.id).values()[0]
#         return Response({
#             "status": status.HTTP_201_CREATED, 
#             'message': "Successfully Created",
#             'data': data},status=status.HTTP_201_CREATED)
          
#     def retrieve(self, request, pk=None):        
#         employee_profiles = EmployeeProfile.objects.filter(id=pk)
#         if not employee_profiles:
#             return Response("invalid employeeprofile", status=status.HTTP_400_BAD_REQUEST)
#         data = employee_profiles.values()
#         print(data)
#         self.serialize(data)
#         return Response(data[0])
    
#     def update(self, request, pk=None):
#         data = request.data
#         employee_profiles = EmployeeProfile.objects.filter(id=pk)
#         if not employee_profiles:
#             return Response("invalid employeeprofile", status=status.HTTP_400_BAD_REQUEST)
#         employee_profile = employee_profiles[0]
#         employee = Employee.objects.filter(id=employee_profile.employee_id)
#         employee_data = data.pop('employee_details')
#         employee.update(**employee_data)
#         team = Team.objects.get(id=employee_profile.team_id)
#         team_name = data.pop("team_name")
#         team.team_name = team_name
#         team.save()
#         employee_profiles.update(**data)
#         return Response({
#             "status": status.HTTP_200_OK,
#             'message': "Successfully updated", 
#             'data':data},status=status.HTTP_200_OK)
        
#     def destroy(self, request, pk=None):
#         try:
#             employee_profile = EmployeeProfile.objects.get(id=pk)
#         except:
#             return Response({
#             "status": status.HTTP_400_BAD_REQUEST,
#             'message': "invalid employee profile", 
#             'data':{}},status=status.HTTP_400_BAD_REQUEST)
#         employee_profile.employee.delete()
#         employee_profile.delete()
#         return Response({
#             "status": status.HTTP_204_NO_CONTENT,
#             'message': "Successfully deleted", 
#             'data':{}},status=status.HTTP_204_NO_CONTENT)
        
        
#     def serialize(self, data):
#         for item in data:
#             employee_id = item.pop("employee_id")
#             employee = Employee.objects.get(id=employee_id)
#             item['employee_details'] = {
#                 "employee_id": employee.id,
#                 "first_name": employee.first_name,
#                 "last_name": employee.last_name,
#                 "email": employee.email,
#                 "phone_number": employee.phone_number
#                 }
#             team_id = item.pop("team_id")
#             team = Team.objects.get(id=team_id)
#             item['team_name'] = team.team_name    

    # def list(self, request):
    #     print("user",request.user)
    #     employee_profiles = EmployeeProfile.objects.all()
    #     data = employee_profiles.values()
    #     self.serialize(data)
    #     return Response(data)
    