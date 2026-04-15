from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Role, User

# ---------- ROLE ----------

@api_view(['GET'])
def get_roles(request):
    return Response(Role.objects.all().values())

@api_view(['POST'])
def add_role(request):
    Role.objects.create(name=request.data.get("name"))
    return Response({"msg": "Added"})

@api_view(['DELETE'])
def delete_role(request, id):
    Role.objects.get(id=id).delete()
    return Response({"msg": "Deleted"})


# ---------- USER ----------

@api_view(['GET'])
def get_users(request):
    users = User.objects.select_related('role', 'department').all()

    data = []
    for u in users:
        data.append({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role.id if u.role else "",
            "role_name": u.role.name if u.role else "",
            "department": u.department.id if u.department else "",
            "department_name": u.department.dept_name if u.department else ""
        })

    return Response(data)


@api_view(['POST'])
def add_user(request):
    User.objects.create(
        name=request.data.get("name"),
        email=request.data.get("email"),
        role_id=request.data.get("role"),
        department_id=request.data.get("department")
    )
    return Response({"msg": "Added"})


@api_view(['PUT'])
def update_user(request, id):
    user = User.objects.get(id=id)

    user.name = request.data.get("name")
    user.email = request.data.get("email")
    user.role_id = request.data.get("role")
    user.department_id = request.data.get("department")

    user.save()
    return Response({"msg": "Updated"})


@api_view(['DELETE'])
def delete_user(request, id):
    User.objects.get(id=id).delete()
    return Response({"msg": "Deleted"})