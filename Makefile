.PHONY: help backend-install backend-run test

help:
	@echo "AegisGrid X development commands"
	@echo "  make backend-install  Install backend dependencies"
	@echo "  make backend-run      Run FastAPI backend"
	@echo "  make test             Run backend tests"

backend-install:
	cd backend && ../.venv/bin/pip install -e ".[dev]"

backend-run:
	cd backend && ../.venv/bin/uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test:
	cd backend && ../.venv/bin/pytest
