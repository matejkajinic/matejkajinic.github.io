---
layout: article
title: 'ProntoPR'
description: 'Autonomous agents that ship incremental features to production through pull requests and CI.'
github_repo: 'matejkajinic/prontopr'
github_url: 'https://github.com/matejkajinic/prontopr'
source_path: 'README.md'
last_commit_sha: '682bdee1f298ea0935dfd52e5e2e958134c89167'
last_commit_date: '2025-07-30T14:01:05Z'
---

<!-- Generated at 2026-05-18T09:41:46Z by scripts/sync_writing.py -->

# ProntoPR - Ship Simple Features

Minimal but extensible prototype demonstrating how a team of specialised autonomous agents can safely ship incremental features to production using GitHub pull-requests, code review, automated tests, and retrieval-augmented generation (RAG).

## Quick start

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install
pip install -e .

# Run (dry-run; does NOT touch GitHub/Docker)
ship-simple-features "Add fibonacci function to utils module" --dry-run

Alternatively, run the standalone demo script:

```bash
python examples/demo.py "Add fibonacci function to utils module" --dry-run
```

 Set `OPENAI_API_KEY` in your environment to enable LLM calls.

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for a Mermaid diagram and detailed explanation.

![Architecture diagram](https://raw.githubusercontent.com/matejkajinic/prontopr/HEAD/docs/diagram.png)

## Configuration

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | API key for OpenAI Chat completions |
| `GITHUB_TOKEN`   | Personal access token for GitHub API (if using real adapter) |
| `GITHUB_REPOSITORY` | `owner/repo` slug for PR creation |

## Development

```bash
# Install dev tools
pip install -r requirements-dev.txt

# Run linters, type-checks, and tests
ruff check .
mypy ship_simple_features
pytest --cov

# Install pre-commit hooks
pre-commit install
```

## License

MIT – see [LICENSE](LICENSE).
