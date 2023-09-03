VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

run: docker-up
	@echo "\33[0;32m collector API is Running!\033[0;32m"

docker-up:
	@docker build -t collector-api .
	@docker-compose up -d

install-poetry: docker-up
	@if ! command -v poetry &>/dev/null; then \
		echo "Installing poetry..."; \
		pip3 install poetry; \
	fi

venv: install-poetry
	@echo "Creating the venv..."
	@poetry install
	$(PIP) install --upgrade pip
	@echo "Starting the virtual environment..."
	@poetry shell

docker-down:
	@docker stop collector-api-ctnr redis-db-collector
	@docker rm -f collector-api-ctnr redis-db-collector
	@docker rmi redis:latest collector-api:latest
	@echo 'docker-down'

clean: docker-down
