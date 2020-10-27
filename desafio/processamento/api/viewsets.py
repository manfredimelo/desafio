
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from processamento.api.serializers import ClassificacaoSerializer
from processamento.models import Classificacao


class ClassificacaoViewSet(ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'produto','regra')

    permission_classes = (DjangoModelPermissions,)

    authentication_classes = (TokenAuthentication,)
    # filter_backends = (SearchFilter,)
    # search_fields = ['id']
    # lookup_field = 'id'
    #
    '''
    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        produto = self.request.query_params.get('id', None)
        # regra = self.request.query_params.get('regra', None)
        queryset = Classificacao.objects.filter(resultado=True)
        if produto:
            queryset = queryset.filter(produto__id=produto)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(ClassificacaoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ClassificacaoViewSet, self).create(request, *args, **kwargs)
    '''