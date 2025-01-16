# Projeto SWAPI

Este projeto é uma API baseada no universo Star Wars, construída com Flask, e utiliza MongoDB para armazenamento de dados. Ele inclui endpoints para gerenciar informações sobre filmes e planetas, e possui testes completos para garantir sua funcionalidade.

## Pré-requisitos

Antes de começar, você precisará ter instalado:

- **Python 3.8+**
- **Pip** (gerenciador de pacotes do Python)
- **MongoDB** (local ou remoto)
- **Make** (opcional, para executar comandos simplificados)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/swapi.git
   cd swapi
   ```

2. Instale as dependências:
   ```bash
   make install
   ```

3. Configure o arquivo `.env` com as seguintes variáveis:
   ```env
   FLASK_APP=app.main:app
   FLASK_ENV=development
   MONGO_URI=mongodb://localhost:27017/swapi
   ```

4. (Opcional) Configure um ambiente virtual:
   ```bash
   make setup
   ```

## Executando a Aplicação

Para iniciar o servidor:

```bash
make run
```

A API estará disponível em: `http://127.0.0.1:5000`

## Endpoints

### Filmes (`/films`)
- `GET /films` - Retorna todos os filmes.
- `GET /films/<id>` - Retorna um filme pelo ID.
- `POST /films` - Cria um novo filme.
- `PUT /films/<id>` - Atualiza um filme existente.
- `DELETE /films/<id>` - Exclui um filme.

### Planetas (`/planets`)
- `GET /planets` - Retorna todos os planetas.
- `GET /planets/<id>` - Retorna um planeta pelo ID.
- `POST /planets` - Cria um novo planeta.
- `PUT /planets/<id>` - Atualiza um planeta existente.
- `DELETE /planets/<id>` - Exclui um planeta.

## Testes

Os testes estão localizados no diretório `tests` e cobrem controllers, rotas, serviços, repositórios e modelos.

### Executando os testes

```bash
make test
```

### Cobertura de Testes

- Controllers
- Routes
- Services
- Repositories
- Models

## Estrutura do Projeto

```plaintext
projeto/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── controllers/
├── tests/
│   ├── test_controllers.py
│   ├── test_routes.py
│   ├── test_services.py
│   ├── test_repositories.py
│   ├── test_models.py
├── requirements.txt
├── Makefile
├── README.md
```

## Limpeza de Arquivos Temporários

Para remover arquivos desnecessários:

```bash
make clean
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Basta criar um fork, fazer suas alterações e enviar um pull request.

