# Comentários sobre a Criação de um Projeto Django

Passos para criar um projeto Django novo:

1. criar o diretório do projeto
2. abrir o diretório no IDLE
    - criar e ativar ambiente virtual
        - usando [`virtualenv`](https://pypi.org/project/virtualenv/)
        - `py -3 -m venv .venv`
    - inicializar git e criar o arquivo .gitignore
3. instalar django
    - `pip install django`
4. verificar se django foi instalado com sucesso
    - `django-admin --version`
5. criar a base do projeto django
    - `django-admin start app .`
6. rodar servidor
    - `python manage.py runserver`
7. adicionar arquivo requirements.txt
    - `pip install -r requirements.txt`

## Apps em  Django

Ao usar  o comando `django-admin start app .`, estamos criando o aplicativo principal, a base e coração do projeto. 

A  criação de  novos apps se dá com base na divisão lógica e responsabilidade do projeto, onde cada app fica responsável por apenas uma única responsabilidade.

![alt text](/docs/div-apps.png)

A criação de um novo app se dá pelo comando `python manage.py startapp nome-do-app`.

Ao criar um novo app, o mesmo deve ser declarado no app principal, no arquivo `settings` em `installed_apps`

## Entendendo os arquivos iniciais

Na raíz:

- manage.py: gerenciador do projeto
- db.sqlite3: banco de dados de desenvolvimento para teste.

No app principal:

- settings.py: configurações gerais do projeto (apps instalados, configuração de banco de dados entre outras)
- urls.py: as rotas do projeto
- asgi e wsgi: quando colocar aplicação em produção, configura aplication server.

Outros apps

- test.py: testes unitários, integração, unittest, pytest, selenium e etc.
- apps.py: configuração do app atual.
- models.py: modelos, tabelas de banco de dados.
- views.py: todas as views (lógica da aplicação).
- admin.py: admin do appp django.


## Inicializar  banco de dados

1. Rastreia arquivos em busca de mudanças:
`python manage.py makemigrations`

2. Executa as mudaças de fato:
`python manage.py migrate`

Sempre que alterar algo no modelo do banco de dados,  execute os passos 1 e 2.


## Criar usuário administrador django (super usuário)

Antes de criar o usuário administrador, inicialize o banco de dados. Após o banco de dados ser inicializado, a criação de super usuário se dá pelo comando:

`python manage.py createsuperuser`

Defina o usuário, email e senha.

### Camadas Urls, views e templates

#### Visão do usuário versus visão do admin

![alt text](/docs/camadas.png)

Usuários e administradores visualizam o sistema de modos diferentes.

admin faz a gestão do conteúdo do site, pela rota, que por padrão é, `admin`

## Django e Banco de Dados

## URLs,Views e Templates

## ORM E Querys no Django

## Forms no Django