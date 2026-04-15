from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.select_related('assigned_to').all()

    data = []
    for t in tasks:
        data.append({
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "user": t.assigned_to.name if t.assigned_to else "Not Assigned"
        })

    return Response(data)


@api_view(['POST'])
def add_task(request):
    Task.objects.create(
        title=request.data.get("title"),
        assigned_to_id=request.data.get("assigned_to")
    )
    return Response({"msg": "Added"})


@api_view(['PUT'])
def update_task(request, id):
    task = Task.objects.get(id=id)

    task.title = request.data.get("title", task.title)
    task.status = request.data.get("status", task.status)

    if request.data.get("assigned_to"):
        task.assigned_to_id = request.data.get("assigned_to")

    task.save()

    return Response({"msg": "Updated"})


@api_view(['DELETE'])
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return Response({"msg": "Deleted"})