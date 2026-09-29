# 🚀 ServiceFlow — Sistema de Gerenciamento de Serviços

&gt; **ServiceFlow** é uma aplicação web voltada ao gerenciamento e acompanhamento centralizado de solicitações de serviços de tecnologia, desde a abertura até a conclusão [4, 7].

---

## 📌 1\. Visão Geral e Problema

Em organizações e equipes de suporte tecnológico, a ausência de um sistema centralizado de atendimento ocasiona perda de informações, falhas no acompanhamento do andamento dos chamados e dificuldades na distribuição de atividades entre os responsáveis [3].

O **ServiceFlow** resolve esse gargalo fornecendo uma plataforma intuitiva conectada a um banco de dados relacional, permitindo organizar solicitações, atribuir técnicos, rastrear o status de cada chamado e gerar indicadores gerenciais da operação [4, 6, 7].

---

## 🛠️ 2\. Tecnologias Utilizadas

O backend e ambiente do projeto são estruturados com as seguintes tecnologias e bibliotecas [33]:

| Tecnologia / Pacote       | Descrição                                                             |
| ------------------------- | --------------------------------------------------------------------- |
| **Python 3.x**            | Linguagem principal do backend.                                       |
| **Django**                | Framework web para estruturação da aplicação e ORM [33].            |
| **Django REST Framework** | Construção de APIs RESTful para integração [33].                    |
| **Psycopg2-binary**       | Conector do banco de dados relacional PostgreSQL [33].              |
| **Django-CORS-Headers**   | Gerenciamento de políticas de CORS para consumo de APIs [33].       |
| **Git / GitHub / Trello** | Controle de versão e gestão visual das Sprints (Kanban) [1, 2, 16]. |

---

## 👥 3\. Perfis de Acesso e Matriz de Permissões

O sistema conta com três perfis principais de usuários autenticados [4, 5, 21]:

1. **Administrador**: Responsável pela gestão de usuários, configurações do sistema e acesso amplo às consultas e relatórios gerenciais [4, 5, 21].
2. **Atendente / Gestor**: Responsável pelo cadastro de clientes, abertura de solicitações, distribuição de chamados para os técnicos e acompanhamento do fluxo [4, 5, 21].
3. **Técnico / Analista**: Responsável por executar os chamados atribuídos, atualizar andamento e registrar observações até a conclusão do serviço [5, 21].

### 📊 Matriz de Casos de Uso (UC01 a UC12)

| Caso de Uso (UC)                     | Descrição                                                | Administrador | Atendente / Gestor | Técnico / Analista |
| ------------------------------------ | -------------------------------------------------------- | ------------- | ------------------ | ------------------ |
| **UC01 — Login**                     | Autenticação no sistema por e-mail e senha [22]        | **✓**         | **✓**              | **✓**              |
| **UC02 — Gerenciar Usuários**        | CRUD e desativação de usuários internos [23]           | **✓**         | —                  | —                  |
| **UC03 — Gerenciar Clientes**        | Cadastro, busca e atualização de clientes [23, 24]     | **✓**         | **✓**              | —                  |
| **UC04 — Gerenciar Categorias**      | Organização das categorias de atendimento [24, 25]     | **✓**         | **✓**              | —                  |
| **UC05 — Abrir Solicitação**         | Registro de novo chamado com cliente/categoria [25]    | **✓**         | **✓**              | —                  |
| **UC06 — Atribuir Serviço**          | Vinculação de um técnico/analista responsável [26]     | **✓**         | **✓**              | —                  |
| **UC07 — Atualizar Status**          | Progressão do ciclo de vida do chamado [27]            | **✓**         | **✓**              | **✓**              |
| **UC08 — Consultar Serviços**        | Listagem com múltiplos filtros combinados [28]         | **✓**         | **✓**              | **✓**              |
| **UC09 — Detalhes do Serviço**       | Detalhamento com histórico e datas [28, 29]            | **✓**         | **✓**              | **✓**              |
| **UC10 — Registrar Observação**      | Registro de notas técnicas durante o atendimento [29]  | **✓**         | **✓**              | **✓**              |
| **UC11 — Visualizar Dashboard**      | Métricas operacionais e contadores por status [29, 30] | **✓**         | **✓**              | —                  |
| **UC12 — Gerenciar Perfil / Logout** | Encerramento seguro de sessão [30]                     | **✓**         | **✓**              | **✓**              |

---

## 🔄 4\. Ciclo de Vida e Fluxo de Status do Chamado

Cada solicitação registrada no **ServiceFlow** segue um fluxo de status controlado e auditável [8, 27]:

```
[ ABERTO ] ➔ [ EM ANÁLISE ] ➔ [ EM ANDAMENTO ] ➔ [ CONCLUÍDO ]
                                        ↳ [ CANCELADO ]

```

* **Aberto**: Status inicial atribuído automaticamente no registro da solicitação [25, 26].
* **Em Análise**: Chamado sob triagem do atendimento ou do técnico.
* **Em Andamento**: Serviço em fase de execução pelo técnico atribuído [27].
* **Concluído**: Serviço finalizado com sucesso e notas de encerramento registradas [5, 27].
* **Cancelado**: Chamado encerrado por inconsistência ou desistência antes da conclusão [27].

---

## 🎯 5\. Delimitação do Escopo

Para garantir a entrega com alta qualidade e dentro dos prazos definidos, o escopo da primeira versão do sistema foi devidamente delimitado [8, 9, 31]:

### ✅ Dentro do Escopo

* Autenticação e controle de perfis de acesso [8, 31].
* Gerenciamento (CRUD) de Usuários, Clientes, Categorias e Serviços [8, 31].
* Atribuição de responsáveis técnicos aos chamados [8, 31].
* Alteração de status e registro de observações de andamento [8, 9, 31].
* Consulta, filtros avançados e histórico básico dos atendimentos [9, 31].
* Dashboard operacional com contadores agrupados [30, 31].
* Banco de dados relacional com restrições e validações de integridade [9, 15, 31].

### ❌ Fora do Escopo (Versão Atual)

* Módulo financeiro completo, faturamento e emissão de notas fiscais [9, 31].
* Aplicativo móvel (iOS / Android) [9, 31].
* Integrações automáticas externas (WhatsApp, e-mails automáticos, Chatbot) [9, 31].
* Mapeamento com Inteligência Artificial ou geolocalização [9, 31].
* Controle automatizado de estoque [9, 31].

---

## 📂 6\. Estrutura do Repositório

Organização dos diretórios do repositório backend [1]:

```
serviceflow-backend/
├── backend/            # Código-fonte da aplicação Django e APIs REST
├── database/           # Scripts de modelagem SQL, migrations e fixtures
├── .gitignore          # Arquivos e pastas ignorados pelo Git
└── requiriments.txt    # Dependências do projeto Python

```

---

## ⚙️ 7\. Instalação e Execução Local

### Pré-requisitos

* Python 3.10+ instalado no ambiente local.

### Passo a Passo

1. **Clonar o Repositório**:  
```  
git clone https://github.com/monteirobgdev/serviceflow-backend.git  
cd serviceflow-backend  
```
2. **Criar e Ativar o Ambiente Virtual (`venv`)**:  
```  
python -m venv venv  
# Windows (PowerShell)  
.\venv\Scripts\activate  
```
3. **Instalar as Dependências**:

  * **Via PyPI (Ambiente Conectado)**:  
  ```  
  pip install -r requiriments.txt  
  ```
  * **Via arquivos `.whl` (Ambiente Corporativo/Offline)**:  
  ```  
  cd backend\Bibliotecas  
  foreach ($f in Get-ChildItem *.whl) { ..\..\venv\Scripts\python.exe -m pip install $f.FullName }  
  cd ..\..  
  ```
4. **Executar Migrações do Banco de Dados**:  
```  
python manage.py migrate  
```
5. **Iniciar o Servidor de Desenvolvimento**:  
```  
python manage.py runserver  
```  
Acesse a API em `http://127.0.0.1:8000/`.
