# desafio_cast
Rota para a API para consulta de classificação de produtos: http://localhost:8000/rotas/classificacoes/




Sobre o desafio proposto:
O desafio
O sistema a ser implementado consiste em um motor de análise de produtos, onde caracteristicas de produtos são analisadas segundo regras cadastradas.

Pode-se dividir o projeto em duas partes:

Motor de análise:

Script (batch) que periódicamente checa se existem produtos não análisados e em caso positivo irá processar a classificação daquele produto.
Os produtos devem ser processados segundo regras. Por exemplo: análisar se o produto tem a caracteristica cor igual a vermelho, e então criar um objeto para registrar este resultado.
Exemplo de funcionamento do motor:
Um produto é cadastrado no banco de dados com as seguintes caracteristicas:
cor: vermelho;
tipo: brinquedo;
codigo_gtin: 12345678
O motor captura o produto recém cadastrado e analisa segundo um conjunto de regras.
Uma regra pode verificar se a cor do produto é vermelha, nesse caso o resultado é positivo.
Para cada regra uma classificação é cadastrada de forma a informar o resultado.
Interface de usuário:

Telas para exibição de resultados e edição de objetos.
Devem ser implementados:

Motor de processamento de regras.
Pelo menos uma das seguintes funcionalidades:
Tela para exibição de produtos, suas caracteristicas e classificações.
Tela para cadastro e edição de regras.
API para consulta de classificação de produtos.
Principais quesistos analisados:

Implementação de testes:
São recomendadas metodologias de implementação como TDD e BDD.
Qualidade do código:
Clareza;
Organização;
Performance.
