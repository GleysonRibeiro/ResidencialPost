# 📁 Estrutura do Projeto

## 📍 Visão Geral

O Sistema de Controle de Correspondências será organizado utilizando a estratégia **Monorepo**, onde todos os componentes do sistema permanecem dentro de um único repositório Git.

Essa abordagem facilita:

- Gerenciamento do projeto;
- Compartilhamento de documentação;
- Integração contínua;
- Evolução simultânea dos módulos.

---

## 🏗️ Organização Geral
condo-correspondence-system/
│
├── docs/
│
├── backend/
│
├── web/
│
├── mobile/
│
├── database/
│
├── infra/
│
├── .gitignore
├── README.md
└── docker-compose.yml


---

## 📚 `/docs`

Contém toda a documentação do projeto.
docs/
├── problema.md
├── mini-mundo.md
├── regras-negocio.md
├── casos-de-uso.md
├── der.md
├── arquitetura.md
├── stack.md
├── product-backlog.md


---

## ⚙️ `/backend`

API responsável pelas regras de negócio.
backend/
├── app/
│ ├── controllers/
│ ├── services/
│ ├── repositories/
│ ├── models/
│ ├── schemas/
│ ├── core/
│ ├── database/
│ └── main.py
│
├── tests/
├── requirements.txt
└── Dockerfile


### Responsabilidades
- Regras de negócio;
- Autenticação;
- API REST;
- Integração com banco.

---

## 🖥️ `/web`

Aplicação Web utilizada pela portaria e administração.
web/
├── src/
│ ├── pages/
│ ├── components/
│ ├── services/
│ ├── routes/
│ ├── hooks/
│ └── App.tsx
│
├── public/
├── package.json
└── Dockerfile


### Responsabilidades
- Interface administrativa;
- Cadastro;
- Controle de entregas;
- Relatórios.

---

## 📱 `/mobile`

Aplicativo destinado aos moradores.
mobile/
├── src/
│ ├── screens/
│ ├── components/
│ ├── services/
│ ├── navigation/
│ └── App.tsx
│
├── assets/
├── package.json
└── app.json


### Responsabilidades
- Consulta de encomendas;
- Notificações;
- Histórico do morador.

---

## 🗄️ `/database`

Arquivos relacionados ao banco de dados.
database/
├── migrations/
├── seeds/
└── schema.sql


---

## ☁️ `/infra`

Configurações de infraestrutura.
infra/
├── docker/
├── nginx/
└── deployment/


---

## 🐳 Docker Compose

O ambiente completo poderá ser iniciado com:
docker-compose up


Serviços previstos:
- Backend API
- Banco PostgreSQL
- Web App

---

## 🌿 Estratégia de Branches
main → produção
develop → integração
feature/* → novas funcionalidades
hotfix/* → correções urgentes


---

## ✅ Benefícios da Estrutura

- Separação clara de responsabilidades;
- Escalabilidade do projeto;
- Facilidade de onboarding;
- Organização profissional;
- Adequado para CI/CD futuro.

