# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, \
#     DjangoObjectPermissions
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from processamento.api.serializers import ClassificacaoSerializer
from processamento.models import Classificacao


class ClassificacaoViewSet(ModelViewSet):
    serializer_class = ClassificacaoSerializer
    filter_backends = (SearchFilter,)
    #permission_classes = (DjangoModelPermissions,)
    #DjangoObjectPermissions
    #authentication_classes = (TokenAuthentication,)

    search_fields = ['id']
    lookup_field = 'produto'

    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        produto = self.request.query_params.get('produto', None)
        regra = self.request.query_params.get('regra', None)
        print('qqqqqqqqqqq', produto, regra)
        queryset = Classificacao.objects.filter(resultado=True)
        print('2222')
        if produto:
            print('22223')
            queryset = queryset.filter(produto__nome__iexact=produto)
            print('22224')

        return queryset

    def list(self, request, *args, **kwargs):
        return super(ClassificacaoViewSet, self).list(request, *args, **kwargs)