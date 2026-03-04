# 🧩 Módulos do Sistema

## 📍 Visão Geral

O Sistema de Controle de Correspondências do Condomínio será dividido em módulos funcionais independentes, permitindo melhor organização, manutenção e evolução do software.

Cada módulo agrupa funcionalidades relacionadas a um contexto específico do sistema.

---

## 🏗️ Estrutura Geral dos Módulos
Sistema de Correspondências
│
├── Módulo Administrativo
├── Módulo Portaria
├── Módulo Morador
├── Módulo Correspondências
├── Módulo Financeiro
├── Módulo Notificações
└── Módulo Segurança e Acesso


---

## 🏢 1. Módulo Administrativo

Responsável pela gestão estrutural do condomínio.

### Funcionalidades
- Cadastro de unidades;
- Cadastro de moradores;
- Cadastro de funcionários;
- Atualização de dados cadastrais;
- Consulta geral do sistema.

### Usuários
- Administrador
- Síndico

---

## 🚪 2. Módulo Portaria

Responsável pela operação diária do sistema.

### Funcionalidades
- Registro de recebimento de correspondência;
- Consulta de encomendas pendentes;
- Registro de entrega;
- Consulta rápida por unidade;
- Identificação do recebedor.

### Usuários
- Porteiros

---

## 📦 3. Módulo Correspondências

Responsável pelo ciclo de vida das encomendas.

### Funcionalidades
- Controle de status:
  - Recebida
  - Aguardando Retirada
  - Entregue
- Histórico de movimentações;
- Rastreamento interno;
- Auditoria de registros.

### Usuários
- Sistema
- Porteiros
- Administradores

---

## 👤 4. Módulo Morador

Disponível no aplicativo mobile.

### Funcionalidades
- Consulta de correspondências recebidas;
- Visualização de histórico;
- Status da encomenda;
- Confirmação de retirada;
- Consulta de pendências.

### Usuários
- Moradores

---

## 💰 5. Módulo Financeiro

Responsável pelo controle de restrições administrativas.

### Funcionalidades
- Registro de pendências financeiras;
- Consulta de situação da unidade;
- Bloqueio de entrega;
- Liberação administrativa.

### Usuários
- Administrador
- Síndico

---

## 🔔 6. Módulo Notificações

Responsável pela comunicação automática com moradores.

### Funcionalidades
- Notificação de nova correspondência;
- Aviso de retirada pendente;
- Atualização de status;
- Integração com push notification.

### Canais previstos
- Push Mobile;
- E-mail;
- SMS (futuro).

---

## 🔐 7. Módulo Segurança e Acesso

Responsável pelo controle de autenticação e autorização.

### Funcionalidades
- Login de usuários;
- Controle por perfil;
- Gestão de permissões;
- Controle de sessão;
- Auditoria de acessos.

### Perfis do Sistema
- Administrador
- Porteiro
- Morador

---

## 🔄 Relação Entre Módulos
Segurança
│
├── Administrativo
│ │
│ └── Financeiro
│
├── Portaria
│ │
│ └── Correspondências
│
└── Morador
│
└── Notificações


---

## ✅ Benefícios da Modularização

- Separação clara de responsabilidades;
- Facilidade de manutenção;
- Escalabilidade funcional;
- Possibilidade de microserviços futuros;
- Melhor organização do código.