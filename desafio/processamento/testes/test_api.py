# -*- encoding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase

class TesteListarCLassificao(APITestCase):


    def teste_listar_filtro_sem_autorizacao(self):
        response = self.client.get('/rotas/classificacoes/?id=1',)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertEqual(Classificacao.objects.get().nome, 'teste')
        self.assertEqual(response['Content-Type'], 'application/json')

    def teste_acessar_api_sem_autorizacao(self):
        response = self.client.get('/rotas/classificacoes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response['Content-Type'], 'application/json')


    # def teste_listar_filtro_com_autorizacao(self):
    #     response = self.client.get('/rotas/classificacoes/?id=1',)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(Classificacao.objects.get().nome, 'teste')
    #     self.assertEqual(response['Content-Type'], 'application/json')
    #
    # def teste_acessar_api_com_autorizacao(self):
    #     response = self.client.get('/rotas/classificacoes/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response['Content-Type'], 'application/json')
