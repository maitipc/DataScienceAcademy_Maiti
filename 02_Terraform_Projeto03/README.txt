Projeto 3 - Deploy do Stack de Infraestrutura de Dados no Azure com Terraform

Neste projeto, trabalhamos com o provedor de cloud computing Microsoft Azure, e usamos o Terraform
para provisionar a infraestrutura de dados através de IaC.

Além disso, usamos o Terraform Graph para visualizar a estrutura e as dependências dos recursos definidos no nosso código:
Acessa o http://webgraphviz.com/
Cola o conteúdo que foi gerado com o comando terraform graph (abaixo) para visualizar o grafo.

Usei um container Docker para realizar esse o deploy na nuvem com o Terraform. O dockerfile não está no repositório.

-------
Lembrando os comandos de deploy do Terraform:

terraform init

terraform validate

terraform plan -out dsa.tfplan

terraform graph

terraform apply dsa.tfplan

terraform destroy