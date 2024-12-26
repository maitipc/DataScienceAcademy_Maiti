Projeto 5 - Databricks Cluster Deploy com Terraform para Processamento Distribuído

Databricks é um provedor de cloud computing. Basicamente é o uso do apache spark na nuvem.
Neste projeto, preparamos a estrutura no Databricks com o Terraform, para executar um script de processamento em linguagem python.

Usei um container Docker para realizar esse o deploy na nuvem com o Terraform. O dockerfile não está no repositório.

-------

No projeto, criamos 3 recursos:

1º - CLUSTER: Para ter o ambiente de processamento (cada cluster é um conjunto de instâncias EC2 no AWS)
2º - NOTEBOOK: Ambiente de processamento para executar o script.
3º - JOB: Script que irá executar o processo no notebook.

-------

# Instalação do Databricks CLI
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh


# Configurar a autenticação:
databricks configure --token

