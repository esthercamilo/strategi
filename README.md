# Projeto Heróis Marvel

Este é um projeto que combina Next.js no frontend e Django no backend para criar uma aplicação web moderna
para o gerenciamento de Heróis Marvel em grupos.

## Descrição

O objetivo da aplicação é o agrupamento de heróis Marvel conforme as seguintes regras:

1. Cada herói deve pertencer a um grupo apenas. 
2. O grupo é uma propriedade associada ao usuário logado. Se no futuro os grupos forem propriedades absolutas, ou seja,
   todos os usuários logados tiverem a capacidade de editar um mesmo grupo, a interface de comunicação deverá ser alterada.
3. A aplicação deve apresentar os heróis sem grupo, um input para escolha do grupo, a possibilidade de cadastro de um novo
   grupo. Tudo isso no formato `ant` design.


## Informações técnicas

O backend foi construído utilizando Django Rest framework




O projeto utiliza a capacidade do Next.js para renderização de páginas dinâmicas e interativas no lado do cliente e servidor,
juntamente com o robusto framework Django para a lógica do backend e gerenciamento de dados.

Um único contêiner Docker abrigar tanto o frontend quanto o backend.
A decisão de começar com um único contêiner foi tomada com base nas necessidades iniciais do projeto,
buscando simplicidade e facilidade de implantação.


## Funcionalidades Principais

- **Next.js (Frontend)**
  - Utiliza a capacidade de SSR e SSG para renderizar páginas de forma eficiente e rápida.
  - Roteamento dinâmico para criação de interfaces de usuário interativas.
  - Utilização de API Routes para comunicação com o backend.

- **Django (Backend)**
  - Framework robusto em Python para a lógica do servidor e gerenciamento de dados.
  - ORM poderoso para interagir com bancos de dados e modelos de dados.
  - Sistema integrado de autenticação e permissões para usuários.

## Como Usar

### Pré-requisitos

- Node.js e npm instalados.
- Python e Django configurados.
- Docker e Docker Compose (opcional para a implantação).

### Instalação

1. **Frontend (Next.js):**
   ```
   cd frontend
   npm install
   npm run dev
   ```

2. **Backend (Django):**
   ```
   cd backend
   pip install -r requirements.txt
   python manage.py runserver
   ```

## Próximos Passos

- Implementar mais funcionalidades no frontend e backend.
- Melhorar a integração entre o Next.js e o Django.
- Considerar a separação dos contêineres Docker para escalabilidade futura.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no projeto.

## Autores

- [Seu Nome] - Desenvolvedor(a) - [Seu GitHub]

## Licença

Este projeto está licenciado sob a [Tipo de Licença]. Consulte o arquivo `LICENSE` para mais detalhes.

---

Adapte este modelo de README com informações específicas do seu projeto, detalhes de configuração, instruções de instalação e outras seções importantes para sua aplicação.






Sinta-se à vontade para adaptar esse texto de acordo com as especificidades do seu projeto e suas preferências.