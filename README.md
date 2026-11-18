# Doubleword provider for Hermes Agent

Adds [Doubleword](https://doubleword.ai) as a model provider in Hermes Agent.

## Install

```bash
hermes plugins install doubleword-provider
```

Get an API key at [app.doubleword.ai](https://app.doubleword.ai) and add it to `~/.hermes/.env`:

```bash
DOUBLEWORD_API_KEY=your-key
```

Then pick Doubleword in `hermes model`, or run:

```bash
hermes chat --provider doubleword --model zai-org/GLM-5.3
```

The model list is fetched from the API. See [docs.doubleword.ai/inference-api/models](https://docs.doubleword.ai/inference-api/models) for what's available.

## What it does

The plugin registers a provider profile and nothing else. Prompts, tool definitions and your `DOUBLEWORD_API_KEY` are sent to `api.doubleword.ai`, or to `DOUBLEWORD_BASE_URL` if you set it. No other network calls, files or background processes.

## License

MIT
