# 🧩 Modelagem do Domínio

## 📍 Visão Geral

A modelagem do domínio tem como objetivo identificar os principais elementos envolvidos no processo de controle de correspondências do condomínio, bem como seus relacionamentos e responsabilidades dentro do contexto do sistema.

As entidades apresentadas foram derivadas a partir da análise do Mini Mundo.

---

## 👥 Atores Envolvidos

Os atores representam os usuários que interagem direta ou indiretamente com o processo.

### Porteiro
Responsável pelo recebimento, registro e entrega das correspondências aos moradores.

### Morador
Destinatário das correspondências e responsável pela retirada das encomendas junto à portaria.

### Síndico / Administrador
Responsável pelo acompanhamento, conferência e controle administrativo das entregas e pendências.

---

## 🏢 Entidades do Domínio

### 🧍 Morador
Representa o residente do condomínio.

**Atributos principais:**
- Identificador do morador
- Nome
- Telefone
- Unidade
- Situação financeira

---

### 🏠 Unidade
Representa o apartamento ou casa pertencente ao condomínio.

**Atributos principais:**
- Identificador da unidade
- Rua
- Número
- Morador responsável

---

### 📦 Correspondência
Representa qualquer encomenda ou correspondência recebida.

**Atributos principais:**
- Identificador da correspondência
- Nome do destinatário
- Tipo de entrega
- Data e hora do recebimento
- Data e hora da entrega
- Retirada por
- Status da entrega


---

### 👮 Funcionário
Representa o colaborador responsável pelas operações na portaria.

**Atributos principais:**
- Identificador do funcionário
- Nome
- Função

---

### 📤 Entrega
Representa o ato de retirada da correspondência pelo morador.

**Atributos principais:**
- Identificador da entrega
- Data e hora da retirada
- Responsável pela entrega
- Confirmação de recebimento
- Recebedor

---

### 💰 Pendência Financeira
Representa possíveis restrições administrativas relacionadas à unidade.

**Atributos principais:**
- Identificador da pendência
- Unidade associada
- Descrição
- Situação
- Data de verificação

---

## 🔗 Relacionamentos

- Um **Morador** ocupa uma **Unidade**;
- Uma **Unidade** pode possuir várias **Correspondências**;
- Uma **Correspondência** é recebida por um **Funcionário**;
- Uma **Correspondência** pode gerar uma **Entrega**;
- Uma **Unidade** pode possuir **Pendências Financeiras**;
- A entrega somente pode ocorrer se não houver impedimentos ativos.


