from rest_framework.serializer import ModelSerializer

from core.models import Acessorios

class AcessorioSerializer(ModelSerializer):
    class meta:
        model =  user
        filds = '__all__'