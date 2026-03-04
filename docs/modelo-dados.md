# 🗄️ Modelo de Dados (DER)

## 📍 Visão Geral

O modelo de dados do ResidencialPost foi construído a partir do modelo de domínio do sistema, garantindo consistência entre regras de negócio, persistência e implementação da API.

O banco de dados adotado é o **PostgreSQL**.

---

# 📦 Entidades e Tabelas

---

## 🏢 CONDOMINIO

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador único |
| nome | VARCHAR(150) | Nome do condomínio |
| endereco | TEXT | Endereço completo |
| cnpj | VARCHAR(20) | Identificação legal |
| data_cadastro | TIMESTAMP | Data de criação |

---

## 🏠 UNIDADE

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| numero | VARCHAR(10) | Número da unidade |
| bloco | VARCHAR(20) | Bloco/Torre |
| observacao | TEXT | Observações |
| condominio_id | UUID | FK Condomínio |

### Relacionamento
- 1 Condomínio → N Unidades

---

## 👤 MORADOR

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| nome | VARCHAR(150) | Nome |
| telefone | VARCHAR(20) | Contato |
| email | VARCHAR(150) | Email |
| status_financeiro | VARCHAR(20) | Situação financeira |
| unidade_id | UUID | FK Unidade |

### Relacionamento
- 1 Unidade → N Moradores

---

## 👮 USUARIO

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| nome | VARCHAR(150) | Nome |
| email | VARCHAR(150) | Login |
| senha_hash | TEXT | Senha criptografada |
| perfil | VARCHAR(30) | Tipo de usuário |
| ativo | BOOLEAN | Status |

---

## 📦 CORRESPONDENCIA

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| descricao | TEXT | Descrição |
| tipo | VARCHAR(50) | Tipo |
| status | VARCHAR(30) | Situação |
| data_recebimento | TIMESTAMP | Recebimento |
| data_entrega | TIMESTAMP | Entrega |
| unidade_id | UUID | FK Unidade |
| recebido_por | UUID | FK Usuário |
| entregue_por | UUID | FK Usuário |

### Relacionamentos
- 1 Unidade → N Correspondências
- 1 Usuário registra recebimento
- 1 Usuário registra entrega

---

## 💰 PAGAMENTO

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| valor | NUMERIC(10,2) | Valor |
| status_pagamento | VARCHAR(20) | Situação |
| data_pagamento | TIMESTAMP | Data |
| correspondencia_id | UUID | FK Correspondência |

### Relacionamento
- 1 Correspondência → 1 Pagamento

---

## 🔔 NOTIFICACAO

| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Identificador |
| tipo | VARCHAR(20) | Canal |
| mensagem | TEXT | Conteúdo |
| data_envio | TIMESTAMP | Envio |
| status_envio | VARCHAR(20) | Status |
| correspondencia_id | UUID | FK Correspondência |

### Relacionamento
- 1 Correspondência → N Notificações

---

# 🔗 Diagrama Conceitual
CONDOMINIO
│
└── UNIDADE
│
└── MORADOR
│
└── CORRESPONDENCIA
├── PAGAMENTO
└── NOTIFICACAO

USUARIO
├── registra_recebimento
└── registra_entrega


---

# 📌 Regras de Integridade

- Correspondência deve possuir unidade válida.
- Entrega só pode ocorrer se pagamento estiver:
  - PAGO ou
  - ISENTO.
- Exclusão de unidade não remove histórico.
- Histórico operacional deve ser preservado.
- Usuário inativo não pode registrar operações.

---

# ✅ Normalização

O modelo encontra-se:

- ✅ 1ª Forma Normal
- ✅ 2ª Forma Normal
- ✅ 3ª Forma Normal

Sem redundâncias estruturais.

---

# 🚀 Preparado Para

- Migrations (Alembic)
- ORM (SQLAlchemy)
- FastAPI Models
- Repositories
- API REST