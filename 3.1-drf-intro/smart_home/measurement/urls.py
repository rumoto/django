from django.urls import path

from measurement.views import SensorView, SensorRetrieveView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path ('sensors/', SensorView.as_view()),
    path ('sensors/<pk>/', SensorRetrieveView.as_view()),
    path ('measurements/', MeasurementView.as_view()),
    path ('measurement/', MeasurementView.as_view()),
]
