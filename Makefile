.PHONY: install test run dev clean

HOST ?= 0.0.0.0
PORT ?= 8000
APP_MODULE := app.main:app

install: ## 依存関係をインストール
	uv sync

dev: ## 開発用依存関係をインストール
	uv sync --dev

test: ## テストを実行
	uv run pytest

test-cov: ## カバレッジ付きテスト
	uv run pytest --cov=app --cov-report=term-missing

run: ## アプリケーション起動
	uv run uvicorn $(APP_MODULE) --host $(HOST) --port $(PORT)

run-dev: ## 開発サーバー起動（ホットリロード）
	uv run uvicorn $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

lint: ## コードチェック
	uv run ruff check app/ tests/

format: ## コードフォーマット
	uv run ruff format app/ tests/

clean: ## キャッシュ削除
	rm -rf .pytest_cache/ htmlcov/ .coverage __pycache__/ *.pyc

all: lint test ## 全チェック実行