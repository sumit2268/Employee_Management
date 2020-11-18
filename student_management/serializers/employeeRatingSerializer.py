from rest_framework import serializers
from ..models import EmployeeRating

class EmployeeRatingSerializer(serializers.ModelSerializer):
    employeeName=serializers.CharField(read_only=True)
    rankingCreteriaName=serializers.CharField(read_only=True)
    reportingManager= serializers.CharField(read_only=True)
    def __init__(self, *args, **kwargs):        
        super(EmployeeRatingSerializer, self).__init__(many=True, *args, **kwargs)
    class Meta:
        fields  = '__all__'
        model   = EmployeeRating
    
    def create(self,validated_data):
        rating = validated_data['rating']
        try:
            employeeRating=EmployeeRating.objects.get(employee=validated_data['employee'],ratingCreteria=validated_data['ratingCreteria'])
            employeeRating.rating = rating
        except EmployeeRating.DoesNotExist:
            employeeRating=EmployeeRating()
            employeeRating.employee=validated_data['employee']
            employeeRating.ratingCreteria=validated_data['ratingCreteria']
            employeeRating.rating = rating
        employeeRating.save()
        return employeeRating

        
