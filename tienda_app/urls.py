from django.urls import path
from .api.views import CompraAPIView
from .views import CompraView, compra_rapida_fbv, CompraRapidaView, CompraRapidaServiceView

urlpatterns = [
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
    path('compra-rapida/<int:libro_id>/', compra_rapida_fbv, name='compra_rapida'),
    path('compra-rapida-cbv/<int:libro_id>/', CompraRapidaView.as_view(), name='compra_rapida_cbv'),
    path('compra-rapida-service/<int:libro_id>/', CompraRapidaServiceView.as_view(), name='compra_rapida_service'),
]