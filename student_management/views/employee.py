from rest_framework import generics
from ..models import Employee
from ..serializers.employeeSerializer import EmployeeSerializer
from django.db.models import F
from rest_framework import filters
from mysite.pagination import ListLimitoffsetPagination

class EmployeeList(generics.ListCreateAPIView):
    queryset=Employee.objects.select_related('reportingEmployee','project').annotate(reportingEmployeeName=F('reportingEmployee__firstName'),projectName=F('project__name')).all()
    serializer_class=EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['firstName','lastName','email','mobileNo','project__name']
    pagination_class=ListLimitoffsetPagination

class EmployeeShow(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.select_related('reportingEmployee','project').annotate(reportingEmployeeName=F('reportingEmployee__firstName'),projectName=F('project__name')).all()
    serializer_class=EmployeeSerializer