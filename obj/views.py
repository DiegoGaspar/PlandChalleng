from rest_framework import viewsets, status
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viajem.objects.all()
    serializer_class = ViagemSerializer

    @api_view(['GET', 'POST'])
    def car_list(request):

        if request.method == 'GET':
            persons = Car.objects.all()
            serializer = CarSerializer(persons, many=True)
            return Response(serializer.fields)

        elif request.method == 'POST':
            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def desgaste_pneu(self):
        self.veiculo.Tyre.estado_degradacao += int(self.distancia / 3)
        return self.veiculo

    def consumo_gas(self):
        pass

"""
