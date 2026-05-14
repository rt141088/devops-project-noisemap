# 🚀 Projeto DevOps — API Containerizada com Azure, Docker e CI/CD

## 📌 Descrição do Projeto

Este projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos modernos de **DevOps**, utilizando infraestrutura em nuvem, containerização e automação de processos através de pipelines CI/CD.

A solução consiste em uma API desenvolvida em **Python** utilizando o framework **Flask**, hospedada em uma Máquina Virtual Linux no **Microsoft Azure** e containerizada com **Docker**. Além disso, foi implementada uma pipeline no **Azure DevOps** para automatizar o processo de integração contínua e validação da aplicação.

---

# 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e ferramentas foram utilizadas no desenvolvimento do projeto:

- Python 3
- Flask
- Docker
- Docker Compose
- Microsoft Azure
- Azure DevOps Pipelines
- GitHub
- Linux Ubuntu 24.04 LTS

---

# ☁️ Infraestrutura em Nuvem

A aplicação foi implantada em uma Máquina Virtual Linux utilizando a plataforma **Microsoft Azure**.

## 🔧 Configurações da Máquina Virtual

| Configuração | Descrição |
|---|---|
| Sistema Operacional | Ubuntu 24.04 LTS |
| Plataforma Cloud | Microsoft Azure |
| Acesso Remoto | SSH |
| Containerização | Docker |
| Exposição da API | Porta HTTP liberada |

---

# 🐳 Containerização com Docker

A aplicação foi totalmente containerizada utilizando **Docker** e **Docker Compose**, permitindo facilidade no deploy, escalabilidade e padronização do ambiente.

## ▶️ Executando o Projeto Localmente

### Subir os containers

```bash
docker-compose up -d --build
Verificar containers em execução
docker ps
🔄 Pipeline CI/CD — Azure DevOps

Foi criada uma pipeline no Azure DevOps responsável pela automação do processo de integração contínua da aplicação.

⚙️ Funcionalidades da Pipeline
Inicialização automática da pipeline
Build automatizado da aplicação Docker
Execução automática do container
Teste automático da API via requisição HTTP
Validação contínua do ambiente
🌐 Acesso da Aplicação

A API pode ser acessada diretamente pelo navegador através do IP público da Máquina Virtual Azure.

🔗 Endpoint Principal
http://64.236.136.233:5000
✅ Resposta Esperada
API rodando com sucesso!
📂 Estrutura do Projeto
devops-project/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── azure-pipelines.yml
└── README.md
📸 Evidências do Projeto

O projeto apresenta as seguintes evidências funcionais:

✅ Pipeline Azure DevOps executando com sucesso
✅ Container Docker em execução na VM Azure
✅ API acessível via navegador
✅ Código versionado no GitHub
✅ Deploy realizado em ambiente Linux na nuvem
✅ Integração contínua funcionando corretamente

👨‍💻 Integrantes
Nome	RM
Rafael Terra Teodoro	RM560955
Enzo Elia Tarraga	RM560901
Otoniel Arantes Barbado	RM560112


🔗 Repositório GitHub
https://github.com/rt141088/devops-project-noisemap

🎯 Objetivo Acadêmico

Este projeto foi desenvolvido para fins acadêmicos com foco na aplicação prática dos seguintes conceitos:

DevOps
Cloud Computing
Docker
CI/CD
Infraestrutura em Nuvem
Containerização
Automação de Deploy
Integração Contínua
Virtualização de Serviços
✅ Conclusão

O projeto demonstra a implementação de uma arquitetura DevOps moderna utilizando Docker, Microsoft Azure e Azure DevOps, permitindo automação de build, execução da aplicação, validação contínua da infraestrutura e maior eficiência no processo de desenvolvimento e deploy.

A utilização de containers e pipelines automatizadas proporciona maior confiabilidade, escalabilidade e padronização do ambiente, aplicando conceitos essenciais utilizados atualmente no mercado de tecnologia.
