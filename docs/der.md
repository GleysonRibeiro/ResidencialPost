# 🗄️ Diagrama Entidade-Relacionamento (DER)

## 📍 Visão Geral

O Diagrama Entidade-Relacionamento (DER) representa a estrutura de dados do sistema de controle de correspondências do condomínio, identificando entidades, atributos e relacionamentos necessários para suportar as regras de negócio definidas.

---

## 🧩 Entidades do Sistema

---

### 🧍 Morador

Representa o residente do condomínio responsável pelo recebimento das correspondências.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_morador | PK | Identificador único |
| nome | Texto | Nome do morador |
| telefone | Texto | Contato |
| email | Texto | E-mail |
| id_unidade | FK | Unidade vinculada |

---

### 🏠 Unidade

Representa apartamentos ou casas do condomínio.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_unidade | PK | Identificador da unidade |
| numero | Texto | Número da unidade |
| bloco | Texto | Bloco ou torre |
| status_financeiro | Texto | Situação da unidade |

---

### 👮 Funcionário

Representa os colaboradores da portaria.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_funcionario | PK | Identificador |
| nome | Texto | Nome |
| funcao | Texto | Cargo |
| turno | Texto | Turno de trabalho |

---

### 📦 Correspondência

Representa encomendas recebidas no condomínio.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_correspondencia | PK | Identificador |
| descricao | Texto | Tipo ou observação |
| data_recebimento | DataHora | Data de chegada |
| status | Texto | Situação da encomenda |
| id_unidade | FK | Unidade destinatária |
| id_funcionario_recebimento | FK | Funcionário responsável |

---

### 📤 Entrega

Representa o registro de retirada da correspondência.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_entrega | PK | Identificador |
| data_entrega | DataHora | Data da retirada |
| recebedor | Texto | Nome do recebedor |
| id_correspondencia | FK | Correspondência entregue |
| id_funcionario_entrega | FK | Funcionário responsável |

---

### 💰 Pendência Financeira

Representa restrições administrativas da unidade.

| Atributo | Tipo | Descrição |
|-----------|------|-----------|
| id_pendencia | PK | Identificador |
| descricao | Texto | Motivo da pendência |
| status | Texto | Ativa/Inativa |
| data_registro | Data | Data da ocorrência |
| id_unidade | FK | Unidade relacionada |

---

## 🔗 Relacionamentos

### Unidade × Morador
- Uma **Unidade** pode possuir **um ou mais moradores**
- Um **Morador** pertence a apenas uma unidade

Unidade (1) -------- (N) Morador


---

### Unidade × Correspondência
- Uma unidade pode receber várias correspondências

Unidade (1) -------- (N) Correspondência


---

### Funcionário × Correspondência
- Um funcionário registra várias correspondências

Funcionário (1) -------- (N) Correspondência


---

### Correspondência × Entrega
- Uma correspondência possui no máximo uma entrega

Correspondência (1) -------- (1) Entrega


---

### Unidade × Pendência Financeira
- Uma unidade pode possuir várias pendências

Unidade (1) -------- (N) Pendência Financeira


---

## 📊 Representação Conceitual Simplificada
Unidade
│
├── Morador
│
├── Correspondência ─── Entrega
│ │
│ └── Funcionário
│
└── Pendência Financeira


---

## ✅ Observações de Modelagem

- Correspondências não devem ser excluídas após entrega;
- O histórico deve ser preservado para auditoria;
- A entrega depende da inexistência de pendência ativa;
- Funcionários diferentes podem registrar recebimento e entrega.

---

## 🎯 Resultado

O DER serve como base para:

- Modelagem do banco de dados;
- Implementação do sistema;
- Criação de APIs e telas;
- Garantia de integridade dos dados.