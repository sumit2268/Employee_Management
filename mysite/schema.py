import graphene
from graphene_django import DjangoObjectType
from student_management.models import Employee

class EmployeeQl(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(EmployeeQl)

schema = graphene.Schema(query=Query)