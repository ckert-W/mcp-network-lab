# MCP Network Lab

A minimal configuration loader used for MCP agent-network experiments.

## Configuration behavior

The application reads an optional user configuration dictionary.

Supported field:

- `timeout`: request timeout in seconds

If the user does not provide a timeout, the loader should use the project default.

## Run tests

```bash
pytest -q
