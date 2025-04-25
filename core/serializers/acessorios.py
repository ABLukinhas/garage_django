from rest_framework.serializer import ModelSerializer

from core.models import Acessorios

class acessorios(ModelSerializer)
    class meta:
        model =  user
        filds = '__all__'