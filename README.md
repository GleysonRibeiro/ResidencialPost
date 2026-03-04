# 📦 ResidencialPost

Sistema de controle de recebimento e entrega de correspondências para condomínios residenciais.

O objetivo do projeto é digitalizar o processo realizado na portaria, garantindo rastreabilidade, segurança e organização na gestão de encomendas e correspondências dos moradores.

---

## 🎯 Problema

Em muitos condomínios, o controle de correspondências ainda é realizado manualmente, gerando problemas como:

- Extravio de encomendas;
- Falta de confirmação de entrega;
- Dificuldade na comunicação com moradores;
- Ausência de controle financeiro associado ao serviço;
- Falta de rastreabilidade para síndicos e administradores.

O **ResidencialPost** surge como solução para automatizar todo o fluxo de recebimento e entrega.

---

## 🚀 Objetivos do Sistema

✅ Registrar recebimento de correspondências  
✅ Notificar moradores automaticamente  
✅ Controlar retirada de encomendas  
✅ Garantir rastreabilidade das entregas  
✅ Controlar permissões financeiras do morador  
✅ Disponibilizar operação via Web e Mobile  

---

## 🏗️ Arquitetura do Sistema

O sistema segue o modelo **Client–Server com API REST centralizada**.
Web App (React)
│
Mobile App (React Native)
│
▼
Backend API (FastAPI)
│
▼
PostgreSQL


### Componentes

- 🌐 Aplicação Web Administrativa
- 📱 Aplicativo Mobile Operacional
- ⚙️ Backend API REST
- 🗄️ Banco de Dados Relacional
- ☁️ Infraestrutura em Nuvem

---

## ⚙️ Stack Tecnológica

### Backend
- Python
- FastAPI
- SQLAlchemy
- JWT Authentication

### Aplicação Web
- React
- TypeScript
- Axios
- React Router
- Material UI

### Aplicativo Mobile
- React Native

### Banco de Dados
- PostgreSQL

### Infraestrutura
- Docker
- Cloud Deployment (AWS / GCP / Azure)
- HTTPS

---

## 🔐 Segurança

- Autenticação baseada em JWT
- Controle de acesso por perfil
- Comunicação segura via HTTPS
- Validação de dados de entrada
- API stateless

---

## 🧪 Testes

| Camada | Tecnologia |
|---|---|
| Backend | Pytest |
| Web | Jest |
| Mobile | React Native Testing Library |

---

## 📚 Documentação

Toda a documentação técnica encontra-se na pasta:

📁 `/docs`

### Conteúdo disponível

- Problema e Objetivos
- Mini Mundo
- Regras de Negócio
- Modelagem de Domínio
- DER
- Arquitetura
- Casos de Uso
- API Endpoints
- Estrutura do Projeto
- Stack Tecnológica
- Product Backlog

---

## 📦 Estrutura do Repositório
ResidencialPost/
│
├── docs/
├── backend/
├── frontend-web/
└── mobile/


---

## 🛠️ Metodologia

O projeto segue práticas modernas de desenvolvimento:

- API First
- Arquitetura em Camadas
- Separação Frontend / Backend
- Versionamento Git Flow
- Documentação orientada a domínio

---

## 👨‍💻 Autor

**Gleyson Ribeiro**

Projeto desenvolvido para estudo, prática de engenharia de software e construção de portfólio profissional.

---

## 📈 Status do Projeto

🚧 Em desenvolvimento — fase de engenharia e modelagem.