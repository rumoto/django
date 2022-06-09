# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


#Получить список датчиков. Создать датчик
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensor_data = SensorDetailSerializer(data=request.data)
        if sensor_data.is_valid():
            sensor_data.save()
        return Response({'status': 'sensor added'})

#Изменить датчик
class SensorRetrieveView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor_object = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'status': 'error'})

#Получить список измерений. Добавить измерение
class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        measurement_data = MeasurementSerializer(data=request.data)
        if measurement_data.is_valid():
            measurement_data.save()
        return Response({'status': 'measurement added'})