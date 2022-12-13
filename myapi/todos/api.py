from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import viewsets 


from .models import Todo
from .serializer import TodoSerializer


class AllTodo(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serilaizer = TodoSerializer(todos, many= True)
        print("serializer: ", serilaizer)
        print("serializer.data: ", serilaizer.data)
        return Response(serilaizer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializor = TodoSerializer(data= request.data)

        if serializor.is_valid():
            serializor.save()
            return Response(serializor.data, status= status.HTTP_201_CREATED)
        print("ERROR: ",serializor.errors)
        return Response(serializor.errors, status=status.HTTP_400_BAD_REQUEST)


class OneTodo(APIView):
    permission_classes = [permissions.AllowAny]
    def get_todo(self, pk):
        try:
            todo = Todo.objects.get(pk= pk)
            return todo
        except Todo.DoesNotExist:
            raise Http404()
    
    def get(self, request, pk):
        # todo = self.get_todo(pk)
        todo = get_object_or_404(Todo, pk= pk)
        ser = TodoSerializer(todo)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        #todo = self.get_todo(pk)
        todo = get_object_or_404(Todo, pk= pk)
        ser = TodoSerializer(todo, data= request.data)

        if ser.is_valid():
            ser.save()
            return Response({"message": "Actualizacón exitosa"}, status= status.HTTP_200_OK)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk, format=None):
        eliminar=self.get_todo(pk)
        eliminar.delete() #Este tiene la funcion de poder eliminar sin hacer la serializacion
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, pk):
        #todo = self.get_todo(pk)
        todo = get_object_or_404(Todo, pk= pk)
        ser = TodoSerializer(todo, data= request.data, partial= True)

        if ser.is_valid():
            ser.save()
            return Response({"message": "Actualizacón exitosa"}, status= status.HTTP_200_OK)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)
    
class TodoViewSetCustom(viewsets.ModelViewSet):

    queryset = Todo.objects.all()

    def get_serializer_class(self):
        return TodoSerializer

    def list(self, request):
        queryset =Todo.objects.all()
        ser = TodoSerializer(queryset, many= True)
        return Response(ser.data)

    def retrieve(self, request, pk= None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        ser = TodoSerializer(todo)
        return Response(ser.data)

    def create(self, request, ):
        if isinstance(request.data, list):
            ser = TodoSerializer(data= request.data, many = True)
        else:
            ser = TodoSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Todo.objects.all()
        todo = get_object_or_404(queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_200_OK)



