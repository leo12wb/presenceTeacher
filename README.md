# API - Gerenciamento de Presenças de professores 

A API de Gerenciamento de Presenças de Professores é uma solução desenvolvida para facilitar o controle e monitoramento da frequência de docentes em instituições de ensino. Com essa API, é possível registrar, atualizar e consultar informações sobre a presença de professores em salas.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o Python instalado em sua máquina. É recomendável usar a versão 3.7 ou superior.

<img align="center" alt="Diagrama de Classes" height="auto" width="100%" src="img.png">

## Passos para Configuração

### 1. Crie um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do seu projeto:

```bash
python -m venv venv

# Ative o ambiente

# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Instale as dependências novamente caso precisar
pip install pydantic mysql-connector-python fastapi uvicorn

# executar
python -m uvicorn main:app --reload

#docker
docker-compose up --build
