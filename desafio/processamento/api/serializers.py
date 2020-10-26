from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from processamento.models import Classificacao


class ClassificacaoSerializer(ModelSerializer):
    # atracoes = AtracaoSerializer(many=True)
    # endereco = EnderecoSerializer()#(read_only=True)
    # comentarios =ComentarioSerializer(many=True, read_only=True)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    # descricao_completa = SerializerMethodField()
    # doc_identificacao = DocIdentificacaoSerializer()
    class Meta:
        model = Classificacao
        fields = '__all__'

        # ready_only_fields = {'comentarios', 'avaliacoes'}
    # def cria_atracoes(self, atracoes, ponto):
    #     for atracao in atracoes:
    #         at =Atracao.objects.create(**atracao)
    #         ponto.atracoes.add(at)
    #     return

    # def create(self, validated_data):
    #
    #
    #     return ''
    # def get_descricao_completa(self, obj):
    #
    #     return '%s - %s ' % (obj.nome, obj.descricao)