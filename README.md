# Marvel Heroes Project [EN]

This is a project that combines Next.js on the frontend and Django on the backend to create a modern web application for managing Marvel Heroes in groups.

## Requirements

The application aims to organize Marvel heroes based on the following rules:

- Each hero should belong to a single group.
- The group is a property associated with the logged-in user. If in the future groups become absolute properties, meaning all logged-in users have the capability to edit the same group, the communication interface must be modified accordingly.
- The application should display heroes without a group, provide an input for choosing a group, and enable the creation of a new group, all in Ant Design format.

## Technical Information [Backend]
The backend was built using Django Rest Framework. This approach is crucial for expediting API development in Django, providing built-in tools for data serialization, authentication, authorization, and validation.

SQLite was used as the database, which is the default option in Django, chosen for its simplicity. The flexibility offered by Django for database switching was also taken into consideration.

Documentation was automatically generated using the drf-yasg (Swagger - OpenAPI) library. This tool simplifies documentation by offering an interactive and readable interface, allowing developers to easily visualize and understand endpoints, methods, parameters, responses, and other essential API information.

Deployment of this application was accomplished through Docker Compose, utilizing three main services:

- Gunicorn: a WSGI server responsible for running the Django application.
- Nginx: a reverse proxy server.
- Frontend: serving the static frontend pages.

Initially, a single composition with separate containers was chosen to host both the frontend and backend based on the initial project requirements, aiming for simplicity and ease of deployment. As the project evolves and more members are needed, this structure should be reviewed.

The backend web application includes basic Django commands and also the `update_marvel_heroes` command, which populates heroes from the official Marvel repository (https://developer.marvel.com/documentation/authorization).

```
python3 manage.py update_marvel_heroes
```

### Token-Based Authentication Workflow

Token-based authentication is used to secure access to protected endpoints in an application. This workflow involves the following steps:

1. **User Login:**
   - User provides their username and password for authentication.
   - Backend authenticates the credentials and generates an access token upon successful authentication.

2. **Token Retrieval:**
   - Upon successful authentication, the backend sends the access token back to the frontend.
   - The frontend securely stores this token, commonly in `sessionStorage` or `localStorage`.

3. **Subsequent Requests:**
   - For subsequent requests to protected endpoints, the frontend includes the stored access token in the `Authorization` header of the HTTP request.
   - The backend validates the token to authorize access to protected resources.

Storing the token in `sessionStorage` maintains it only for the current browser session, while `localStorage` persists it across sessions. Proper security measures such as HTTPS implementation and token expiration handling should be considered for secure token management.

This token-based workflow ensures secure access to authenticated resources while allowing seamless user interactions within the application.

## Usage

The documentation details can be found on the Swagger page of the project. The local address can be http://127.0.0.1:8000/api.

### Installation

The prerequisites for installing this application are:
1. Docker Engine (https://docs.docker.com/engine/install/).
2. Docker Compose (https://docs.docker.com/desktop/install/ubuntu/)

You can build the composition as you are accustomed to.

Suggested command for Linux systems:

`$ docker-compose up --build -d`



