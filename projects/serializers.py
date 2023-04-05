from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #datos a acceder
        fields = ('id','title','description','technology','created_at')
        #datos de solo lectura, osea que no se modifiquen, por ejemplo esto es la fecha de creacion, lo cual no se puede modificar
        #debo ponerle la coma al final pq sino lo va a poner como una string y debe ser una tupla
        read_only = ('created_at',)