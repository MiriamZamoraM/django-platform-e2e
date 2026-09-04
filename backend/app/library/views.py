from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import Libros
from .serializers import LibroSerializer

# Create your views here.

class LibroAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class LibrosRetrieve(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        libros_list = Libros.objects.all()
        return Response(libros_list, status.HTTP_200_OK)