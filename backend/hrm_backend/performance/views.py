from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Performance

@api_view(['GET'])
def get_performance(request):
    data = Performance.objects.select_related('user').all()

    result = []
    for p in data:
        result.append({
            "id": p.id,
            "user": p.user.name,
            "rating": p.rating,
            "review": p.review
        })

    return Response(result)


@api_view(['POST'])
def add_performance(request):
    Performance.objects.create(
        user_id=request.data.get("user"),
        rating=request.data.get("rating"),
        review=request.data.get("review")
    )
    return Response({"msg": "Added"})

@api_view(['DELETE'])
def delete_performance(request, id):
    Performance.objects.get(id=id).delete()
    return Response({"msg": "Deleted"})