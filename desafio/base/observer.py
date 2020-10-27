import schedule
import time
from base.models import Produto
from processamento.models import Regra, Classificacao

''' método para iniciar a classficação de produtos não avaliados'''
def motor():
    # schedule.every(10).minutes.do(analise_classificao)
    schedule.every().hour.do(analise_classificao)
    # schedule.every().day.at("10:30").do(analise_classificao)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(analise_classificao)
    # schedule.every().minute.at(":17").do(analise_classificao)

    while True:
        schedule.run_pending()
        time.sleep(1)

'''revisa classificações dadas após edição de uma regra'''
def revisa_classificacoes_regra(regra):

    produtos = Produto.objects.filter()

    for produto in produtos:
        '''Atualizando as classificações existentes'''
        classificacoes = Classificacao.objects.filter(regra=regra, produto=produto)
        if classificacoes:
            for classificacao in classificacoes:

                if (classificacao.regra.campo == 'cor' and classificacao.regra.valor == produto.cor) or \
                        classificacao.regra.campo == 'tipo' and classificacao.regra.valor == produto.tipo:
                    classificacao.resultado = True
                else:
                    classificacao.resultado = False
                classificacao.save()
        else:

            nova_classificao(regra, produto)
    return

'''revisa classificações dadas após edição de um produto'''
def revisa_classificacoes_produto(produto):

    regras = Regra.objects.filter()
    for regra in regras:
        '''Atualizando as classificações existentes'''
        classificacoes = Classificacao.objects.filter(regra=regra, produto=produto)
        if classificacoes:
            for classificacao in classificacoes:

                if (classificacao.regra.campo == 'cor' and classificacao.regra.valor == produto.cor) or \
                        classificacao.regra.campo == 'tipo' and classificacao.regra.valor == produto.tipo:
                    classificacao.resultado = True
                else:
                    classificacao.resultado = False
                classificacao.save()
        else:

            nova_classificao(regra, produto)

    return

'''faze nova classificação'''
def nova_classificao(regra, produto):
    classificacao = Classificacao()
    if (regra.campo == 'cor' and regra.valor == produto.cor) or \
            regra.campo == 'tipo' and regra.valor == produto.tipo:
        classificacao.resultado = True

    else:
        classificacao.resultado = False
    classificacao.regra = regra
    classificacao.produto = produto

    produto.processado = True
    produto.save()
    return

def analise_classificao(regra=None, produto=None):
    produtos = Produto.objects.filter(processado=False)
    if regra:
        revisa_classificacoes_regra(regra)
    elif produto:
        revisa_classificacoes_produto(produto)
    else:
        regras = Regra.objects.all()
        for regra in regras:

            for produto in produtos:
                nova_classificao(regra, produto)
