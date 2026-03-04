# ⚙️ Stack Tecnológico

## 📍 Visão Geral

Este documento define o conjunto de tecnologias adotadas para o desenvolvimento do Sistema de Controle de Correspondências do Condomínio.

A escolha da stack foi baseada nos seguintes critérios:

- Alta produtividade;
- Facilidade de manutenção;
- Escalabilidade;
- Comunidade ativa;
- Aderência a arquiteturas modernas Web e Mobile.

---

## 🏗️ Estrutura Geral do Sistema

O sistema será composto por:

- Backend (API REST)
- Aplicação Web
- Aplicativo Mobile
- Banco de Dados
- Infraestrutura em Nuvem

---

## ⚙️ Backend

### Linguagem
**Python**

### Framework
**FastAPI**

#### Justificativa
- Alto desempenho;
- Suporte nativo a APIs REST;
- Documentação automática (Swagger/OpenAPI);
- Tipagem forte;
- Facilidade de integração com aplicações modernas.

---

### ORM
**SQLAlchemy**

Responsável pelo mapeamento objeto-relacional e comunicação com o banco de dados.

---

### Autenticação
**JWT (JSON Web Token)**

Permite:
- Sessões stateless;
- Compartilhamento de autenticação entre Web e Mobile;
- Segurança baseada em tokens.

---

## 🖥️ Aplicação Web

### Linguagem
**JavaScript / TypeScript**

### Framework Frontend
**React**

#### Bibliotecas auxiliares
- Axios → consumo da API
- React Router → navegação
- Material UI → componentes visuais

---

## 📱 Aplicativo Mobile

### Tecnologia
**React Native**

#### Justificativa
- Código compartilhado com React Web;
- Desenvolvimento multiplataforma;
- Redução de tempo de desenvolvimento;
- Manutenção simplificada.

---

## 🗄️ Banco de Dados

### SGBD
**PostgreSQL**

#### Motivos
- Alta confiabilidade;
- Suporte a relacionamentos complexos;
- Controle transacional;
- Escalabilidade.

---

## 🔄 Comunicação

### Padrão
API RESTful

### Formato de Dados
JSON

---

## ☁️ Infraestrutura e Deploy

### Backend
- Docker
- Hospedagem em Cloud (AWS, GCP ou Azure)

### Banco de Dados
- PostgreSQL gerenciado em nuvem

### Aplicação Web
- Deploy via Vercel ou Netlify

### Aplicativo Mobile
- Distribuição via:
  - Google Play Store
  - Apple App Store

---

## 🔐 Segurança

- HTTPS obrigatório;
- Autenticação JWT;
- Controle de acesso baseado em perfis;
- Validação de entrada de dados;
- Proteção contra acesso não autorizado.

---

## 🧪 Testes

### Backend
- Pytest

### Frontend
- Jest

### Mobile
- React Native Testing Library

---

## 📦 Controle de Versão

### Plataforma
GitHub

### Estratégia
Git Flow simplificado:
- main
- develop
- feature/*
- release/*
- hotfix/*

---

## 🚀 Ferramentas de Desenvolvimento

- Git
- Docker
- VS Code
- Postman / Insomnia
- Figma (protótipos)

---

## ✅ Benefícios da Stack Escolhida

- Reutilização de conhecimento entre Web e Mobile;
- Backend único para múltiplos clientes;
- Facilidade de evolução futura;
- Arquitetura escalável;
- Padrões amplamente utilizados no mercado.