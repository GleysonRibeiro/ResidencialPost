# 🎭 Casos de Uso

## 📍 Visão Geral

Os casos de uso descrevem as funcionalidades do sistema sob a perspectiva dos usuários, demonstrando como cada ator interage com o sistema de controle de correspondências do condomínio.

---

## 👥 Atores do Sistema

### Porteiro
Responsável pelo registro, controle e entrega das correspondências.

### Morador
Destinatário das correspondências e responsável pela retirada.

### Administrador / Síndico
Responsável pelo acompanhamento, conferência e gestão das informações do sistema.

---

## 📋 Lista de Casos de Uso

| Código | Caso de Uso |
|--------|-------------|
| UC01 | Cadastrar Morador |
| UC02 | Cadastrar Unidade |
| UC03 | Registrar Recebimento de Correspondência |
| UC04 | Consultar Correspondências Pendentes |
| UC05 | Verificar Pendência Financeira |
| UC06 | Registrar Entrega de Correspondência |
| UC07 | Consultar Histórico |
| UC08 | Gerar Relatórios |

---

## 📦 UC01 – Cadastrar Morador

**Ator Principal:** Administrador  
**Descrição:** Permite cadastrar moradores vinculados às unidades do condomínio.

### Fluxo Principal
1. O administrador acessa o cadastro de moradores;
2. Informa os dados do morador;
3. Associa o morador a uma unidade;
4. O sistema valida as informações;
5. O sistema salva o cadastro.

---

## 🏠 UC02 – Cadastrar Unidade

**Ator Principal:** Administrador  

### Fluxo Principal
1. O administrador informa os dados da unidade;
2. O sistema registra a unidade no condomínio;
3. A unidade fica disponível para associação a moradores.

---

## 📥 UC03 – Registrar Recebimento de Correspondência

**Ator Principal:** Porteiro  

### Fluxo Principal
1. O porteiro acessa o sistema;
2. Seleciona a unidade ou morador destinatário;
3. Informa os dados da correspondência;
4. O sistema registra data e hora automaticamente;
5. O sistema define o status como **Aguardando Retirada**;
6. A correspondência é armazenada.

---

## 🔎 UC04 – Consultar Correspondências Pendentes

**Ator Principal:** Porteiro  

### Fluxo Principal
1. O porteiro realiza consulta por unidade ou morador;
2. O sistema apresenta as correspondências pendentes;
3. O porteiro localiza o volume armazenado.

---

## 💰 UC05 – Verificar Pendência Financeira

**Ator Principal:** Porteiro  

### Fluxo Principal
1. O porteiro seleciona a correspondência;
2. O sistema verifica a situação da unidade;
3. O sistema informa se existe impedimento para entrega.

---

## 📤 UC06 – Registrar Entrega de Correspondência

**Ator Principal:** Porteiro  

### Fluxo Principal
1. O morador solicita retirada;
2. O porteiro localiza a correspondência;
3. O sistema verifica pendências;
4. O porteiro confirma o recebedor;
5. O sistema registra data e hora da entrega;
6. O status é atualizado para **Entregue**.

### Fluxo Alternativo
**A1 – Existência de pendência**
- O sistema bloqueia a entrega;
- A correspondência permanece pendente.

---

## 📊 UC07 – Consultar Histórico

**Ator Principal:** Administrador  

### Fluxo Principal
1. O administrador acessa o histórico;
2. Seleciona filtros de consulta;
3. O sistema apresenta registros de recebimento e entrega.

---

## 📈 UC08 – Gerar Relatórios

**Ator Principal:** Administrador  

### Fluxo Principal
1. O administrador seleciona o tipo de relatório;
2. Define período ou unidade;
3. O sistema gera relatório de movimentações.

---

## ✅ Relacionamento Geral dos Atores
Administrador ──► Cadastros
Administrador ──► Relatórios

Porteiro ──► Receber Correspondência
Porteiro ──► Entregar Correspondência
Porteiro ──► Consultar Pendências

Morador ──► Retirar Correspondência


---

## 🎯 Resultado Esperado

A definição dos casos de uso permite:

- Identificar funcionalidades do sistema;
- Construir diagramas UML;
- Definir backlog de desenvolvimento;
- Orientar implementação e testes.