# 📦 Modelo de Domínio

## 📍 Visão Geral

O modelo de domínio representa as entidades principais envolvidas no processo de controle de correspondências dentro do condomínio.

O sistema foi modelado com base no mini mundo e nas regras de negócio definidas para o ResidencialPost.

---

## 🧩 Entidades do Domínio

---

## 🏢 Condomínio

Representa o ambiente onde o sistema opera.

### Atributos
- id
- nome
- endereco
- cnpj
- dataCadastro

### Responsabilidades
- Agrupar unidades residenciais
- Centralizar operações administrativas

---

## 🏠 Unidade

Representa um apartamento ou casa dentro do condomínio.

### Atributos
- id
- numero
- bloco
- observacao
- condominioId

### Responsabilidades
- Associar moradores
- Receber correspondências

---

## 👤 Morador

Representa o residente responsável pela unidade.

### Atributos
- id
- nome
- telefone
- email
- statusFinanceiro
- unidadeId

### Responsabilidades
- Receber notificações
- Retirar correspondências
- Possuir situação financeira válida

---

## 👮 Usuário

Representa operadores do sistema.

### Tipos
- Porteiro
- Administrador
- Síndico

### Atributos
- id
- nome
- email
- senhaHash
- perfil
- ativo

### Responsabilidades
- Registrar recebimentos
- Registrar entregas
- Consultar informações

---

## 📦 Correspondência

Entidade central do sistema.

Representa qualquer encomenda ou correspondência recebida.

### Atributos
- id
- descricao
- tipo
- dataRecebimento
- dataEntrega
- status
- unidadeId
- recebidoPor
- entreguePor

### Status possíveis
- RECEBIDA
- NOTIFICADA
- ENTREGUE
- CANCELADA

### Responsabilidades
- Controlar ciclo de vida da encomenda
- Garantir rastreabilidade

---

## 💰 Pagamento

Representa valores associados ao recebimento ou armazenamento da correspondência.

### Atributos
- id
- valor
- dataPagamento
- statusPagamento
- correspondenciaId

### Status
- PENDENTE
- PAGO
- ISENTO

### Responsabilidades
- Validar liberação da entrega
- Permitir conferência administrativa

---

## 🔔 Notificação

Representa avisos enviados ao morador.

### Atributos
- id
- tipo
- mensagem
- dataEnvio
- statusEnvio
- correspondenciaId

### Tipos
- EMAIL
- APP
- SMS

### Responsabilidades
- Informar chegada da correspondência
- Registrar histórico de comunicação

---

## 🔄 Relacionamentos
Condomínio
└── Unidade
└── Morador
└── Correspondência
├── Pagamento
└── Notificação

Usuário
├── recebe Correspondência
└── entrega Correspondência


---

## 📌 Regras de Domínio Importantes

- Uma correspondência pertence a uma única unidade.
- Uma unidade pode possuir vários moradores.
- A entrega só pode ocorrer se:
  - não houver pendência financeira; ou
  - o pagamento estiver quitado.
- Toda correspondência deve possuir histórico de recebimento.
- O sistema deve manter rastreabilidade completa da operação.

---

## ✅ Resultado da Modelagem

Este modelo será utilizado como base para:

- Modelagem do Banco de Dados
- Criação das Entidades Backend
- Definição da API REST
- Construção das interfaces Web e Mobile