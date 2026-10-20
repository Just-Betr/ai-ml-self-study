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
setx PYTHONUTF8 1             # Windows only, once: stops UnicodeEncodeError crashes on emoji output
uv sync                       # creates .venv and installs everything from uv.lock
cp .env.example .env          # then fill in your own keys
uv run ruff check . && uv run ruff format --check . && uv run pytest
```

## Local services

Postgres 16 and the MLflow tracking server run in Docker (needs Docker Desktop running and
`POSTGRES_PASSWORD` set in `.env`). Both restart with Docker and only listen on this machine.

```bash
docker compose up -d          # start both; data persists in the pgdata and mlartifacts volumes
docker compose ps             # both should say (healthy)
docker compose exec postgres psql -U study -d study
docker compose down           # stop (add -v to wipe the data)
```

- Postgres: connect from code with `DATABASE_URL` from `.env` (`localhost:5432`).
- MLflow: UI at http://127.0.0.1:5000. In code, `mlflow.set_tracking_uri("http://127.0.0.1:5000")`.
  Runs are stored in the `mlflow` database in Postgres; artifacts go through the server into the
  `mlartifacts` volume.

Local Kubernetes with kind (needs Docker running):

```bash
kind create cluster --name study    # once; sets kubectl's context to kind-study
kubectl get nodes
kind delete cluster --name study    # tear down
```

Notebooks: `uv run jupyter lab`.
