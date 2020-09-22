from rest_framework.viewsets import ModelViewSet
from .serializers import BurgerSerializer
from .models import Burger


class BurgerViewSet(ModelViewSet):
    serializer_class = BurgerSerializer
    queryset = Burger.objects.all()