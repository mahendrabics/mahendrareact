

from django.shortcuts import render
from rest_framework import viewsets         
from .serializers import StudentSerializer     
from .models import Student  
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class TodoView(viewsets.ModelViewSet):      
    serializer_class = StudentSerializer       
    queryset = Student.objects.all()
    
    
class YourListView(APIView):
    def get(self, request, *args, **kwargs):
        total_workhours_per_project = Student.objects.values('projectname').annotate(total_workhours=Sum('workhours'))
        return Response(total_workhours_per_project)
    



