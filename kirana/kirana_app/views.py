from rest_framework.views import APIView
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from .services import AddItemService


# Create your views here.

class AddItem(APIView):
    def post(self, request):
        serial_data = ItemSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            serialized_data = serial_data.validated_data
            item_create = AddItemService.execute({
                "name": serialized_data.get("name"),
                "category": serialized_data.get("category"),
                "price": serialized_data.get("price"),
                "description": serialized_data.get("description"),
            }
            )
            return Response({"sucess": item_create}, status.HTTP_200_OK)


class ListViewItem(APIView):
    def get(self, request):
        try:
            item = Item.objects.all()
            serial_data = ItemSerializer(item, many=True)
            return Response({"result": serial_data.data}, status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({"fail":"empty data"}, status.HTTP_400_BAD_REQUEST)