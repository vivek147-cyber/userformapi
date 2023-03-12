from urllib import response
from rest_framework import generics,status
from rest_framework.response import Response
from .models import UserForm
from .serializers import UserSerializer


class CreateView(generics.CreateAPIView):
    queryset = UserForm.objects.all()
    serializer_class = UserSerializer

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_form = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        contacts = self.get_queryset()
        serializer = self.get_serializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    