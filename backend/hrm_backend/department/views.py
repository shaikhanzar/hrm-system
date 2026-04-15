from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer

@api_view(['GET'])
def get_departments(request):
    data = Department.objects.all()
    return Response(DepartmentSerializer(data, many=True).data)

@api_view(['POST'])
def add_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_department(request, id):
    dept = Department.objects.get(id=id)
    serializer = DepartmentSerializer(dept, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_department(request, id):
    dept = Department.objects.get(id=id)
    dept.delete()   # or status=False
    return Response({"msg": "Deleted"})