# 🚀 Projeto DevOps — API Containerizada com Azure, Docker, PostgreSQL e CI/CD

---

# 📌 Descrição do Projeto

Este projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos modernos de **DevOps**, utilizando infraestrutura em nuvem, containerização e automação de processos através de pipelines CI/CD.

A solução consiste em uma API desenvolvida em **Python** utilizando o framework **Flask**, hospedada em uma Máquina Virtual Linux no **Microsoft Azure** e containerizada com **Docker**. Além disso, foi implementada uma pipeline no **Azure DevOps** para automatizar o processo de integração contínua, validação da aplicação e deploy automatizado.

O sistema também utiliza **PostgreSQL** como banco de dados relacional, garantindo persistência real dos dados em ambiente cloud.

---

# 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e ferramentas foram utilizadas no desenvolvimento do projeto:

- Python 3
- Flask
- PostgreSQL
- SQLAlchemy
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
| Banco de Dados | PostgreSQL |
| Exposição da API | Porta 5000 liberada |

---

# 🐳 Containerização com Docker

A aplicação foi totalmente containerizada utilizando **Docker** e **Docker Compose**, permitindo facilidade no deploy, escalabilidade e padronização do ambiente.

---

# 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** como banco de dados principal, executando em container Docker na infraestrutura Azure.

## 📋 Estrutura Relacional

O sistema possui duas tabelas principais:

### 👤 usuarios
Responsável pelo armazenamento dos usuários cadastrados na aplicação.

Campos:
- id
- nome

### 📢 denuncias
Responsável pelo armazenamento das denúncias registradas.

Campos:
- id
- descricao
- usuario_id

## 🔗 Relacionamento

Uma denúncia pertence a um usuário através da chave estrangeira:

```sql
usuario_id → usuarios.id
```

O banco de dados possui persistência real em ambiente cloud.

---

# 🔄 CRUD da API

A aplicação disponibiliza endpoints REST para operações CRUD.

## 📌 Endpoints

### Criar usuário

```http
POST /usuarios
```

### Listar usuários

```http
GET /usuarios
```

### Criar denúncia

```http
POST /denuncias
```

### Listar denúncias

```http
GET /denuncias
```

---

# ▶️ Executando o Projeto Localmente

## 📦 Subir os containers

```bash
docker-compose up -d --build
```

## 🔍 Verificar containers em execução

```bash
docker ps
```

---

# 🔄 Pipeline CI/CD — Azure DevOps

Foi criada uma pipeline no Azure DevOps responsável pela automação do processo de integração contínua da aplicação.

## ⚙️ Funcionalidades da Pipeline

- Inicialização automática da pipeline
- Build automatizado da aplicação Docker
- Execução automática do container
- Teste automático da API via requisição HTTP
- Validação contínua do ambiente
- Integração contínua com GitHub

---

# 🌐 Acesso da Aplicação

A API pode ser acessada diretamente pelo navegador através do IP público da Máquina Virtual Azure.

## 🔗 Endpoint Principal

```bash
http://64.236.136.233:5000
```

---

# ✅ Resposta Esperada

```json
API rodando com sucesso!
```

---

# 📂 Estrutura do Projeto

```bash
devops-project/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── azure-pipelines.yml
├── modelo.pkl
├── templates/
│   └── index.html
└── README.md
```

---

# 📸 Evidências do Projeto

O projeto apresenta as seguintes evidências funcionais:

✅ Pipeline Azure DevOps executando com sucesso  
✅ Container Docker em execução na VM Azure  
✅ API acessível via navegador  
✅ Código versionado no GitHub  
✅ Deploy realizado em ambiente Linux na nuvem  
✅ Integração contínua funcionando corretamente  
✅ Persistência real utilizando PostgreSQL  
✅ CRUD funcionando corretamente  
✅ Banco de dados relacional com tabelas relacionadas  

---

# 🔐 Segurança e Infraestrutura

A infraestrutura possui:

- VM Linux Ubuntu no Azure
- Comunicação via SSH
- Porta 5000 liberada no NSG do Azure
- Containers isolados via Docker
- Banco de dados executando em container dedicado

---

# 👨‍💻 Integrantes

| Nome | RM |
|---|---|
| Rafael Terra Teodoro | RM560955 |
| Enzo Elia Tarraga | RM560901 |
| Otoniel Arantes Barbado | RM560112 |

---

# 🔗 Repositório GitHub

:contentReference[oaicite:0]{index=0}

---

# 🎥 Vídeo Demonstrativo

O vídeo demonstrativo apresenta:

- Execução da pipeline Azure DevOps
- Funcionamento da API
- Containers Docker em execução
- Persistência dos dados
- CRUD funcionando
- Infraestrutura em nuvem no Azure

---

# 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido para fins acadêmicos com foco na aplicação prática dos seguintes conceitos:

- DevOps
- Cloud Computing
- Docker
- CI/CD
- Infraestrutura em Nuvem
- Containerização
- Automação de Deploy
- Integração Contínua
- Virtualização de Serviços
- Persistência de Dados em Nuvem

---

# ✅ Conclusão

O projeto demonstra a implementação de uma arquitetura DevOps moderna utilizando Docker, PostgreSQL, Microsoft Azure e Azure DevOps, permitindo automação de build, execução da aplicação, validação contínua da infraestrutura e maior eficiência no processo de desenvolvimento e deploy.

A utilização de containers, banco de dados relacional e pipelines automatizadas proporciona maior confiabilidade, escalabilidade e padronização do ambiente, aplicando conceitos essenciais utilizados atualmente no mercado de tecnologia.

Além disso, o projeto evidencia a utilização prática de serviços em nuvem, persistência real de dados e integração contínua, atendendo os requisitos técnicos exigidos para a Sprint 4 da disciplina DevOps Tools & Cloud Computing.
