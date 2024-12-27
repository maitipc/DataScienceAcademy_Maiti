 :::: Projeto  de  Multi-Cloud Deploy: deploy em dois provedores de Cloud Computing de forma simultânea ::::


 Deploy multi-cloud refere-se a prática de distribuir aplicações, serviços e recursos entre varias plataformas de computação em nuvem.

 O Terraform possui a capacidade de lidar com múltiplos provedores de serviços em  nuvem de maneira consistente e eficiente.

 Este projeto une os conceitos estudados para demonstrar como um  único  projeto  com  Terraform  pode  ser  usado para  o  deploy  em diferentes  provedores  de Cloud Computing de forma simultânea. O Multi-Cloud Deploy aumenta de forma  considerável a complexidade de um processo IaC, pois teremos que lidar com diferentes procedimentos de autenticação, diferentes providers, diferentes  tipos  de  recursos  e  diferentes  configurações.

 -----

 ::: ESTRUTURA DO PROJETO :::

 1. MÓDULO DE PROVIDERS: providers.tf
 	Usado para definir e configurar o ambiente de IaC em provedores de nuvem específicos (no caso, AWS e Azure).
 	Colocamos todas as conexões aos provedores de Cloud Computing em um único arquivo de providers.
 	
 2. MÓDULO DE VARIÁVEIS: variables.tf
 	Define as variáveis necessárias para o provisionamento de recursos, abrangendo tanto AWS quanto Azure.

 3. MÓDULO PARA INSTÂNCIA AWS: aws.tf
 	Configura uma infraestrutura completa na AWS, incluindo VPC, subnets, internet gateway, tabela de roteamento, load balancer, grupos de segurança e uma instância EC2, proporcionando uma base sólida para a implementação de aplicações na AWS.

 4. MÓDULO PARA INSTÂNCIA AZURE: azure.tf
 	Configura uma infraestrutura na Azure, incluindo grupo de recursos, rede vitual, subnet, IP público, interface de rede e uma máquina virtual, fornecendo uma base robusta para a execução de aplicativos na nuvem.


 ::: EXECUÇÃO :::

Criar um container docker que tenha AWS CLI e Azure CLI instalados. Usar o AWS Configure para configurar as credenciais da AWS e o az login para efetuar o login na Azure. Configurar as chaves de segurança nos arquivos do terraform.
Após criar o container e efetuar login nos provedores cloud, executar os comandos do terraform:

init
plan
apply
destroy