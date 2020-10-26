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
    #     atracoes = validated_data['atracoes']
    #     del validated_data['atracoes']
    #     endereco = validated_data['endereco']
    #     del validated_data['endereco']
    #
    #     doc_identificacao = validated_data['doc_identificacao']
    #     del validated_data['doc_identificacao']
    #
    #     ponto = PontoTuristico.objects.create(**validated_data)
    #     self.cria_atracoes(atracoes, ponto) #'''Processando manytomany'''
    #     end = Endereco.objects.create(**endereco) #Processando foreignkey
    #     ponto.endereco = end
    #
    #
    #     doc_identificacao = DocIdentificacao.objects.create(**doc_identificacao)
    #     ponto.doc_identificacao = doc_identificacao
    #
    #     return ponto
    # def get_descricao_completa(self, obj):
    #
    #     return '%s - %s ' % (obj.nome, obj.descricao)