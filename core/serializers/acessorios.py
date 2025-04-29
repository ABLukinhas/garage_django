from rest_framework.serializers import ModelSerializer

from core.models import Acessorios

class AcessoriosSerializer(ModelSerializer):
    class meta:
        model =  Acessorios
        fields = '__all__'