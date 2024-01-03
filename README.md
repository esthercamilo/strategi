# Projeto Heróis Marvel \[PT\]

Este é um projeto que combina Next.js no frontend e Django no backend para criar uma aplicação web moderna
para o gerenciamento de Heróis Marvel em grupos.

## Requisitos

O objetivo da aplicação é o agrupamento de heróis Marvel conforme as seguintes regras:

1. Cada herói deve pertencer a um grupo apenas. 
2. O grupo é uma propriedade associada ao usuário logado. Se no futuro os grupos forem propriedades absolutas, ou seja,
   todos os usuários logados tiverem a capacidade de editar um mesmo grupo, a interface de comunicação deverá ser alterada.
3. A aplicação deve apresentar os heróis sem grupo, um input para escolha do grupo, a possibilidade de cadastro de um novo
   grupo. Tudo isso no formato `ant` design.


## Informações técnicas \[backend\]

O backend foi construído utilizando Django Rest Framework. Essa abordagem é crucial para agilizar o desenvolvimento
de APIs no Django, oferecendo ferramentas integradas para serialização de dados, autenticação, autorização e validação.

Como banco de dados, foi utilizado SQLite. Essa opção é default do Django e foi motivada por simplicidade. A 
flexibilidade oferecida pelo Django para a troca de banco de dados também foi levada em consideração.

A documentação foi gerada automaticamente utilizando a biblioteca drf-yasg (Swagger - OpenAPI).
Esta ferramenta simplifica a documentação, oferecendo uma interface interativa e legível,
permitindo que desenvolvedores visualizem e compreendam facilmente os endpoints, métodos,
parâmetros, respostas e outras informações essenciais da API.

A implantação desta aplicação foi realizada por meio do Docker Compose, usando três serviços principais:

1. Gunicorn: servidor WSGI responsável por executar a aplicação Django;
2. Nginx: servidor proxy reverso
3. Frontend: disponibilização das páginas estáticas do frontend

Optou-se inicialmente por uma única composição, porém containers separados, para abrigar tanto o frontend quanto o backend com base nas 
necessidades iniciais do projeto, buscando simplicidade e facilidade de implantação. A medida que o projeto evolui 
e mais membros são necessários essa estrutura deve ser revista. 

A aplicação web backend possui os comandos básicos do Django e também o comando `update_marvel_heroes` que popula
os heróis a partir do repositório oficial Marvel (https://developer.marvel.com/documentation/authorization)

```
python3 manage.py update_marvel_heroes
```

## Utilização

Os detalhes da documentação podem ser encontrados na página Swagger do projeto

### Instalação

Os pré-requisito para instalação dessa aplicação são:
1. docker engine (https://docs.docker.com/engine/install/).
2. docker-compose (https://docs.docker.com/desktop/install/ubuntu/)

Você pode fazer o build da composição como está habituado. 

Passos sugeridos (sistema linux):

`$ docker-compose up --build -d`



