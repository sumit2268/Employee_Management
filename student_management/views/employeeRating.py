from rest_framework import generics
from ..models import EmployeeRating
from ..serializers.employeeRatingSerializer import EmployeeRatingSerializer
from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
class EmployeeRatingList(generics.ListCreateAPIView):
    queryset=EmployeeRating.objects.select_related('employee','ratingCreteria','employee__reportingEmployee').annotate(employeeName=F('employee__firstName'),rankingCreteriaName=F('ratingCreteria__rankingName'),reportingManager=F('employee__reportingEmployee__id')).all()
    serializer_class=EmployeeRatingSerializer
    def post(self,request,*args,**kwargs):
        serializer = EmployeeRatingSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


class EmployeeRatingShow(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeRating.objects.select_related('employee','ratingCreteria').annotate(employeeName=F('employee__firstName')).all()
    serializer_class=EmployeeRatingSerializer