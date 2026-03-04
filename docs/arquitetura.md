# 🏗️ Arquitetura do Sistema

## 📍 Visão Geral

O Sistema de Controle de Correspondências do Condomínio será desenvolvido utilizando uma arquitetura moderna baseada em aplicações distribuídas, composta por:

- Aplicação Web;
- Aplicativo Mobile;
- API Backend Centralizada;
- Banco de Dados Relacional.

Essa arquitetura permite escalabilidade, manutenção facilitada e reutilização dos serviços entre diferentes plataformas.

---

## 🧩 Modelo Arquitetural

O sistema seguirá o padrão:

✅ Arquitetura em Camadas (Layered Architecture)  
✅ Backend orientado a serviços (API REST)  
✅ Separação entre Frontend e Backend  

---


---

## 🖥️ Aplicação Web

Destinada aos usuários administrativos.

### Usuários
- Porteiros
- Administradores
- Síndico

### Responsabilidades
- Cadastro de moradores;
- Cadastro de unidades;
- Registro de recebimento;
- Registro de entrega;
- Consulta de histórico;
- Geração de relatórios;
- Controle financeiro.

---

## 📱 Aplicativo Mobile

Destinado aos moradores do condomínio.

### Funcionalidades
- Consulta de correspondências recebidas;
- Notificação de novas encomendas;
- Histórico de retiradas;
- Status de entrega;
- Visualização de pendências.

---

## ⚙️ Backend (API)

O Backend será responsável por centralizar toda a lógica do sistema.

### Responsabilidades
- Implementação das regras de negócio;
- Autenticação e autorização;
- Controle de acesso;
- Processamento das requisições;
- Comunicação com banco de dados;
- Integração entre Web e Mobile.

### Padrão adotado
API RESTful.

---

## 🗄️ Banco de Dados

Será utilizado banco relacional para garantir integridade e consistência.

### Tecnologia sugerida
PostgreSQL.

### Responsabilidades
- Persistência dos dados;
- Relacionamentos entre entidades;
- Controle transacional;
- Auditoria histórica.

---

## 🔐 Segurança

O sistema adotará:

- Autenticação baseada em token (JWT);
- Controle de permissões por perfil:
  - Administrador
  - Porteiro
  - Morador
- Comunicação segura via HTTPS.

---

## 🔄 Fluxo de Comunicação

### Recebimento de Correspondência
1. Porteiro registra via aplicação Web;
2. Web envia requisição para API;
3. API valida regras de negócio;
4. Dados são persistidos no banco;
5. API envia confirmação;
6. Morador recebe notificação no App Mobile.

---

### Entrega de Correspondência
1. Morador solicita retirada;
2. Porteiro registra entrega;
3. API verifica pendências;
4. Status atualizado no banco;
5. Histórico mantido.

---

## 🧱 Arquitetura Interna do Backend

O Backend seguirá separação por camadas:

Controller
↓
Service
↓
Repository
↓
Database


### Controller
Recebe requisições HTTP.

### Service
Contém regras de negócio.

### Repository
Responsável pelo acesso aos dados.

### Database
Persistência das informações.

---

## 🚀 Escalabilidade

A arquitetura permite:

- Expansão para múltiplos condomínios;
- Integração com sistemas financeiros;
- Inclusão de novos aplicativos;
- Implantação em nuvem.

---

## ✅ Benefícios da Arquitetura

- Separação de responsabilidades;
- Reutilização da API;
- Manutenção simplificada;
- Escalabilidade horizontal;
- Suporte multiplataforma.