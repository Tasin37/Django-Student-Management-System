from django.shortcuts import render

# Create your views here.
from faculty.models import *
from faculty.serializers import *
from rest_framework.response import Response
from rest_framework import  mixins, generics,viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class DepartmentListCreateApiView(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["building"]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class DepartmentUpdateDeleteApiView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherApiViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    ordering_fields = ["salary"]

class ResultApiViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class DepartmentHeadApiViewSet(viewsets.ModelViewSet):
    queryset = DepartmentHead.objects.all()
    serializer_class = DepartmentHeadSerializer