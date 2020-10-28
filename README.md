
Rota para a API para consulta de classificação de produtos: http://localhost:8000/rotas/classificacoes/


Foram feitos: Listagem, cadastro e edição de regras e produtos. Cada regra ou produto modificado faz com que as classificações sejam refeitas/alteradas ou até mesmo criada.
Na lista de produto é possivel clicar na opção de visualizar classificação.
A view observer mantém todo o motor de classificação. Pode ser rodado chamando a def motor() que usa a biblioteca schedule e rodará a análise a cada hora. Pode ser rodado também através da def analise_classificao() que fará toda a verificação. Para isto, a análise da classificação deverá estar configurada em um cron no servidor.



Foi usada a biblioteca do django TestCase para a cobertura de alguns testes unitários.
Para rodar: python manage.py test  ou python manage.py test --verbosity 2




Sobre o desafio proposto:

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
