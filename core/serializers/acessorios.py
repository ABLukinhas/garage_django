from core.views import acessorios
from rest_framework.serializers import ModelSerializer

from core.models import Acessorios

class AcessoriosSerializer(ModelSerializer):
    class meta:
        model =  Acessorios
        filds = '__all__'