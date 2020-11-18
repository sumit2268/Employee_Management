from rest_framework import viewsets
from ..models import Project
from ..serializers.projectSerializer import ProjectSerializer

class ProjectList(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer