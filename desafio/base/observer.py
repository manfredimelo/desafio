import schedule
import time
from base.models import Produto
from processamento.models import Regra, Classificacao


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

def analise_classificao():
    produtos = Produto.objects.filter(processado=False)
    regras = Regra.objects.all()
    for regra in regras:

        for produto in produtos:

            classificacao = Classificacao()
            if (regra.campo == 'cor' and regra.valor == produto.cor) or\
                    regra.campo == 'tipo' and regra.valor == produto.tipo:
                classificacao.resultado = True

            else:
                classificacao.resultado = False
            classificacao.regra = regra
            classificacao.produto = produto
            classificacao.save()

            produto.processado = True
            produto.save()
