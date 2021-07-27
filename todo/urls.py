
from django.urls import path
from todo.views import get_todos, create_todo, delete_todo, id_lookup

urlpatterns = [
    path('', get_todos, name='get_todos'),
    path('create-todo/', create_todo, name='create-todo'),
    path('delete-todo/<int:id>/', delete_todo, name='delete-todo'),
    path('id-lookup/', id_lookup, name='id-lookup'),
]
