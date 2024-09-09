Lab 4 - Deploy de Infraestrutura e API Para Aplicação de Data Science na AWS com Terraform
# Criação do Modelo de Machine Learning
# Modelo de Classificação - Considerando o valor das 4 compras anteriores de um cliente, prever se ele vai realizar outra compra (Sim/Não)


Este lab implica em realizar um processo completo de automação de uma aplicação com uma API,
fazendo a interação entre o front-end (página web) e o back-end (modelo de Machine Learning).

Primeiro fizemos o deploy local para testar a aplicação e, na sequência, construímos o processo de automação com o Terraform para fazer o deploy na nuvem, na AWS.

Na AWS:
Usamos o S3 para armazenar e recuperar os objetos que utilizamos (no caso, o conteúdo da pasta /dsa_ml_app),
E usamos uma instância EC2 (servidor virtual na nuvem) para fazer uma cópia desses objetos que estavam no bucket e executá-los.

Usei um container Docker para realizar esse o deploy na nuvem com o Terraform nesse laboratório. O dockerfile não está no repositório.

-----

PARA TESTAR LOCALMENTE:
Dentro do diretório /dsa_ml_app:

python app.py
