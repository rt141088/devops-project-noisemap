# 🚀 Projeto DevOps — NoiseMap API Containerizada com Azure, Docker, SQLite e CI/CD

---

## 📌 Descrição do Projeto

Este projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos modernos de **DevOps**, utilizando infraestrutura em nuvem, containerização e automação de processos através de pipelines CI/CD.

A solução consiste em uma **API REST** desenvolvida em **Python** com o framework **Flask**, voltada ao registro de denúncias de ruídos urbanos (**NoiseMap**). A aplicação está hospedada em uma Máquina Virtual Linux no **Microsoft Azure**, containerizada com **Docker** e integrada ao **Azure DevOps Pipelines** para automação de build e deploy.

O sistema utiliza **SQLite** como banco de dados, com persistência real em ambiente cloud dentro do container Docker.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão |
|---|---|
| Python | 3.x |
| Flask | 3.x |
| SQLAlchemy | 3.x |
| SQLite | 3.x |
| Docker | 27.x |
| Docker Compose | 2.x |
| Microsoft Azure | VM Linux |
| Azure DevOps Pipelines | - |
| GitHub | - |
| Linux Ubuntu | 24.04 LTS |

---

## ☁️ Infraestrutura em Nuvem

| Configuração | Descrição |
|---|---|
| Sistema Operacional | Ubuntu 24.04 LTS |
| Plataforma Cloud | Microsoft Azure |
| Acesso Remoto | SSH / Azure Bastion |
| Containerização | Docker + Docker Compose |
| Banco de Dados | SQLite (persistido no container) |
| IP Público da API | 64.236.136.233 |
| Porta exposta | 5000 |

---

## 🗄️ Banco de Dados

O projeto utiliza **SQLite** com duas tabelas relacionadas.

### 👤 Tabela: `usuario`

| Campo | Tipo |
|---|---|
| id | INTEGER (PK) |
| nome | VARCHAR |

### 📢 Tabela: `denuncia`

| Campo | Tipo |
|---|---|
| id | INTEGER (PK) |
| descricao | VARCHAR |
| usuario_id | INTEGER (FK → usuario.id) |

### 🔗 Relacionamento

```sql
denuncia.usuario_id → usuario.id
```

---

## 🔄 Endpoints da API

### Base URL

```
http://64.236.136.233:5000
```

### Usuários

```http
GET  /usuarios          → Lista todos os usuários
POST /usuarios          → Cria um novo usuário
```

**Body POST /usuarios:**
```json
{
  "nome": "Rafael"
}
```

### Denúncias

```http
GET  /denuncias         → Lista todas as denúncias
POST /denuncias         → Cria uma nova denúncia
```

**Body POST /denuncias:**
```json
{
  "descricao": "Ruido alto na Av. Paulista",
  "usuario_id": 1
}
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

- Docker
- Docker Compose
- Git

### 1. Clonar o repositório

```bash
git clone https://github.com/rt141088/devops-project-noisemap.git
cd devops-project-noisemap
```

### 2. Subir os containers

```bash
sudo docker-compose up -d --build
```

### 3. Verificar containers em execução

```bash
sudo docker ps
```

### 4. Testar a API

```bash
curl http://localhost:5000
curl http://localhost:5000/usuarios
curl http://localhost:5000/denuncias
```

### 5. Criar dados de teste

```bash
curl -X POST http://localhost:5000/usuarios \
  -H "Content-Type: application/json" \
  -d '{"nome": "Rafael"}'

curl -X POST http://localhost:5000/denuncias \
  -H "Content-Type: application/json" \
  -d '{"descricao": "Ruido alto na Av. Paulista", "usuario_id": 1}'
```

### 6. Verificar persistência no banco

```bash
sudo docker exec -it devops-project_web_1 python3 -c \
  "import sqlite3; conn = sqlite3.connect('instance/devops.db'); \
  cur = conn.cursor(); \
  cur.execute('SELECT * FROM usuario'); print('USUARIOS:', cur.fetchall()); \
  cur.execute('SELECT * FROM denuncia'); print('DENUNCIAS:', cur.fetchall()); \
  conn.close()"
```

---

## 🔄 Pipeline CI/CD — Azure DevOps

A pipeline foi configurada no **Azure DevOps** e executa automaticamente as seguintes etapas:

| Etapa | Descrição |
|---|---|
| Checkout | Clona o repositório do GitHub |
| Docker Build | Constrói a imagem Docker da aplicação |
| Docker Run | Sobe o container na porta 5000 |
| Health Check | Testa se a API responde com sucesso |

### Arquivo de configuração

`azure-pipelines.yml` — disponível no repositório.

---

## 📂 Estrutura do Projeto

```
devops-project-noisemap/
│
├── app.py                  # API Flask com rotas e modelos
├── Dockerfile              # Configuração do container
├── docker-compose.yml      # Orquestração dos containers
├── requirements.txt        # Dependências Python
├── azure-pipelines.yml     # Pipeline CI/CD Azure DevOps
├── scripts-api/
│   └── scripts-api.md      # Scripts JSON para teste do CRUD
└── README.md
```

---

## ✅ Evidências do Projeto

✅ Pipeline Azure DevOps executando com sucesso (build verde)
✅ Container Docker em execução na VM Azure
✅ API acessível via IP público: `http://64.236.136.233:5000`
✅ CRUD completo funcionando (usuarios e denuncias)
✅ Duas tabelas com relacionamento (FK) no banco de dados
✅ Persistência real de dados provada via SQLite
✅ Código versionado no GitHub com README
✅ Scripts JSON do CRUD disponíveis em `/scripts-api`

---

## 👨‍💻 Integrantes

| Nome | RM |
|---|---|
| Rafael Terra Teodoro | RM560955 |
| Enzo Elia Tarraga | RM560901 |
| Otoniel Arantes Barbado | RM560112 |

---

## 🔗 Repositório GitHub

[https://github.com/rt141088/devops-project-noisemap](https://github.com/rt141088/devops-project-noisemap)

---

## 🎥 Vídeo Demonstrativo

[ cole aqui o link do YouTube após gravar ]

O vídeo apresenta:
- Execução da pipeline no Azure DevOps
- API respondendo via IP público
- CRUD completo (POST e GET de usuarios e denuncias)
- Persistência dos dados no banco SQLite
- Infraestrutura em nuvem no Azure

---

## 🎯 Objetivo Acadêmico

Projeto desenvolvido para a **Sprint 4 — DevOps Tools & Cloud Computing (FIAP)**, com foco na aplicação prática de:

- DevOps e CI/CD
- Cloud Computing (Microsoft Azure)
- Containerização com Docker
- Automação de Deploy via Azure DevOps Pipelines
- Persistência de Dados em Nuvem
- Integração Contínua com GitHub
