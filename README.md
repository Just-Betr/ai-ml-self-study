# ai-ml-self-study

A self-paced AI & ML study plan worked as five portfolio projects, from a tabular ML pipeline to deployed LLM agents.

| Folder | Project |
| --- | --- |
| [`01-pulse/`](01-pulse/) | Pulse: ingestion, features, training, notebooks |
| [`02-pulse-service/`](02-pulse-service/) | Pulse service: FastAPI app, worker, Docker, k8s manifests |
| [`03-carescribe/`](03-carescribe/) | CareScribe: data curation, fine-tuning notebooks, evals |
| [`04-resolve/`](04-resolve/) | Resolve: agent graph, MCP server, RAG, red-team suite |
| [`05-atlas/`](05-atlas/) | Atlas: Flutter web dashboard, integration, deploy |

Specs, design docs, decision records and the weekly log live in [`docs/`](docs/).

## Setup

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows; use .venv/bin/activate on macOS/Linux
pip install -e ".[dev]"
cp .env.example .env          # then fill in your own keys
ruff check . && ruff format --check . && pytest
```
