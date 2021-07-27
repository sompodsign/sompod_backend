from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoSerializer
from .models import Todo
import json


@api_view(['GET'])
def get_todos(request):
    todos = Todo.objects.all()
    return Response(todoSerializer(todos, many=True).data)


@api_view(['POST'])
def create_todo(request):
    data = json.loads(request.body)
    try:
        id = int(data['highestId'])
    except:
        try:
            id = Todo.objects.all().order_by("-_id")[0]._id + 1
        except:
            id = 1
    todo = Todo.objects.create(
        _id=id,
        title=data['title'],
        date=data['date'],
        month=data['month'],
        year=data['year'],
    )
    todo.save()
    return Response({"details": "successfully created!"})


@api_view(['GET'])
def id_lookup(request):
    try:
        id = Todo.objects.all().order_by("-_id")[0]._id + 1
    except:
        id = 1
    return Response({"id": id})


@api_view(['DELETE'])
def delete_todo(request, id):
    try:
        todo_to_delete = Todo.objects.get(_id=id)
        todo_to_delete.delete()
    except:
        Response({'details': 'item does not exist'})
    return Response({"Details": "Successfully deleted"})
