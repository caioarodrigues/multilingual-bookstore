# Multilingual Bookstore API
Choose a language:
[English](#multilingual-bookstore-api) | [Português](#biblioteca-multilíngue-api)

## Overview

Multilingual Bookstore is an API built with Python 3.13 and FastAPI, designed to manage a platform of books in multiple languages. This application allows authenticated users to create, read, update, and delete books, as well as manage the chapters of each book.

## Features

- **Secure user authentication**
- **Management of books in multiple languages**
- **Creation and editing of chapters by book**
- **Favorite books marking system**
- **Admin panel**

## Data Model

The application uses SQLAlchemy as an ORM to interact with the database. The data model consists of:

### User
- User registration and authentication
- Author profile for book publishing
- Saving favorite books in different languages

### Book
- Basic information such as title
- Association with an author (user)
- Support for multiple languages
- Organization into chapters

### Chapter
- Chapter title and content
- Association with a specific book
- Chapter language definition

### Language
- Catalog of languages available on the platform
- Identification by name and abbreviation

## Requirements

- Python 3.13+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn (ASGI server)
- SQLite3

## Installation

1. Clone the repository:
```bash
git clone https://github.com/caioarodrigues/multilingual-bookstore.git
cd multilingual-bookstore
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the server:
```bash
uvicorn main:app --reload
```

## API Usage

### Authentication

```
POST /login
```

### Books

```
GET /books - List all books
GET /books/{id} - Get book details
POST /books/add - Create new book
PUT books/{id} - Update book
DELETE books/{id} - Delete book
```

### Languages

```
GET /languages - List all available languages
```

### Users

```
GET /users - List all users
GET /users/me - Get current user profile
GET /users/{id}/ - List info by user id
GET /users/books/list-all - List all books saved by user 
GET /users/{id}/books/ - List books by an specific author id  
POST /users - Create new user
POST /users/books/save - Save a new book to a user
DELETE /users - Remove user
PATCH /users - Edit user
```

## Documentation

Interactive API documentation is available at:
- Swagger UI: http://0.0.0.0:8000/docs

## Contribution

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# Biblioteca Multilíngue API

[English](#multilingual-bookstore-api) | [Português](#biblioteca-multilíngue-api)

## Visão Geral

Biblioteca Multilíngue é uma API construída com Python 3.13 e FastAPI, projetada para gerenciar uma plataforma de livros em múltiplos idiomas. Esta aplicação permite que usuários autenticados criem, leiam, atualizem e excluam livros, bem como gerenciem os capítulos de cada livro.

## Recursos

- **Autenticação segura de usuários**
- **Gerenciamento de livros em múltiplos idiomas**
- **Criação e edição de capítulos por livro**
- **Sistema de marcação de livros favoritos**
- **Painel de administração**

## Modelo de Dados

A aplicação utiliza SQLAlchemy como ORM para interagir com o banco de dados. O modelo de dados consiste em:

### Usuário (User)
- Registro e autenticação de usuários
- Perfil de autor para publicação de livros
- Salvamento de livros favoritos em diferentes idiomas

### Livro (Book)
- Informações básicas como título
- Associação com um autor (usuário)
- Suporte para múltiplos idiomas
- Organização em capítulos

### Capítulo (Chapter)
- Título e conteúdo do capítulo
- Associação com um livro específico
- Definição do idioma do capítulo

### Idioma (Language)
- Catálogo de idiomas disponíveis na plataforma
- Identificação por nome e abreviação

## Requisitos

- Python 3.13+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn (servidor ASGI)
- SQLite3

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/caioarodrigues/multilingual-bookstore.git
cd multilingual-bookstore
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:
```bash
alembic upgrade head
```

5. Inicie o servidor:
```bash
uvicorn main:app --reload
```

## Uso da API

### Autenticação

```
POST /login
```

### Livros

```
GET /books - Listar todos os livros
GET /books/{id} - Obter detalhes de um livro
POST /books/add - Criar novo livro 
PUT books/{id} - Atualizar livro 
DELETE books/{id} - Excluir livro 
```


### Idiomas

```
GET /languages - Listar todos os idiomas disponíveis
```

### Usuários

```
GET /users - Lista todos os usuários
GET /users/me - Obter perfil do usuário atual
GET /users/{id}/books - Listar livros de um autor
POST /users - Cria novo usuário
DELETE /users - Remove usuário
PATCH /users - Edita usuário 
```

## Documentação

A documentação interativa da API está disponível em:
- Swagger UI: http://0.0.0.0:8000/docs

## Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.