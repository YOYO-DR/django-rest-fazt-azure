from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    #allowany es para todos, pero puedo ponerle el IsAuthenticated para preguntar si esta autenticado 
    permission_classes=[permissions.AllowAny]
    serializer_class = ProjectSerializer