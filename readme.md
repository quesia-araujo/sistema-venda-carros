# Sobre o Projeto

Projeto Django direcionado a um sistema web para vendas de carros.

## Entendendo decisões arquiteturais e a estrutura do projeto

### Requisitos para rodar o projeto

#### Setup de ambiente:

- Crie um ambiente virtual em python
    - Usando [`virtualenv`](https://pypi.org/project/virtualenv/)
        - `py -3 -m venv .venv`
    - Ative o ambiente virtual
        - `.venv/Scripts/activate` (windows)
        - `.venv/bin/activate` (linux)

#### Como rodar na minha máquina?

- Clone o projeto
- Instale a dependencias do projeto
    - `pip install -r requirements.txt`
- Crie um usuário admin (opicional)
- Rode o servidor
    - `python manage.py runserver`

### Estrutura do projeto

O projeto está subdividido em apps,  onde cada app é responsável por uma funcionalidade do sistema.

- `app` - o app base, contendo as configurações gerais do projeto.
- `cars` - um app que tem a função de gerenciar o cadastro e CRUD (Create, Read, Uptade e Delete) de carros da base de dados do sistema.
- `docs` - uma pasta onde estão arquivos referentes a documentação do projeto. 
- `media` ficam armazenadas as midias fornecidas pelo upload de usuários.
    - `cars` - imagens fornecidas pelos usuário de carros cadastrados no sistema.


### Models

A tabela car possui os seguintes dados sobre os carros do sistema:

- id (int - auto incrementável)
- modelo (string)
- marca (chave estrangeira da tabela marca)
- ano de fabricação (int)
- ano do  modelo (int)
- placa (string)
- valor (float)
- foto (imagem)

A tabela brand possui os seguintes campos:

- id (int - auto incrementável)
- marca  (string)

### Views e URLs

O acesso para visão de usuário se dará pela rota `cars/`. 
O usuário terá acesso a uma barra de pesquisa, onde poderá filtrar os resultados de exibição pelo modelo do carro.

No arquivo [create new project](), faço comentários sobre a criação de novos projetos em Django.