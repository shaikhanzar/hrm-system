from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Leave

# GET
@api_view(['GET'])
def get_leave(request):
    leaves = Leave.objects.select_related('user').all()

    data = []
    for l in leaves:
        data.append({
            "id": l.id,
            "user": l.user.name,
            "reason": l.reason,
            "start_date": l.start_date,
            "end_date": l.end_date,
            "status": l.status
        })

    return Response(data)


# ADD
@api_view(['POST'])
def add_leave(request):
    Leave.objects.create(
        user_id=request.data.get("user"),
        reason=request.data.get("reason"),
        start_date=request.data.get("start_date"),
        end_date=request.data.get("end_date"),
    )
    return Response({"msg": "Added"})


# UPDATE STATUS
@api_view(['PUT'])
def update_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = request.data.get("status")
    leave.save()
    return Response({"msg": "Updated"})


# DELETE
@api_view(['DELETE'])
def delete_leave(request, id):
    Leave.objects.get(id=id).delete()
    return Response({"msg": "Deleted"})