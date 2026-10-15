from rest_framework.views import APIView
from rest_framework.response import Response

from tienda_app.models import Libro
from tienda_app.api.serializers import LibroSerializer


class ProductosAPIView(APIView):
    """Lista los libros (productos) del monolito Django (v1)."""

    def get(self, request):
        libros = Libro.objects.all()
        return Response(LibroSerializer(libros, many=True).data)