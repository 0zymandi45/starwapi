PYTHON = python
PIP = pip
APP_MODULE = app.main:app
TESTS_DIR = tests
ENV = .venv

install:
	@echo "Instalando dependências..."
	$(PIP) install -r requirements.txt

run:
	@echo "Iniciando a aplicação..."
	$(PYTHON) -m flask run --app $(APP_MODULE)

test:
	@echo "Executando testes..."
	pytest $(TESTS_DIR)

setup:
	@echo "Criando ambiente virtual e instalando dependências..."
	$(PYTHON) -m venv $(ENV)
	$(ENV)/bin/$(PIP) install -r requirements.txt

clean:
	@echo "Limpando arquivos temporários..."
	rm -rf $(ENV)
	rm -rf __pycache__
	rm -rf $(TESTS_DIR)/__pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache

help:
	@echo "Comandos disponíveis:"
	@echo "  install  - Instala as dependências do projeto"
	@echo "  run      - Inicia a aplicação Flask"
	@echo "  test     - Executa os testes com pytest"
	@echo "  setup    - Cria o ambiente virtual e instala as dependências"
	@echo "  clean    - Remove arquivos e diretórios temporários"
