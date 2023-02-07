# ChatGPT Client

[![Latest Release](https://img.shields.io/github/v/release/vsakkas/chatgpt-client.svg)](https://github.com/vsakkas/chatgpt-client/releases/tag/0.1.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/vsakkas/chatgpt-client/blob/master/LICENSE)
[![CI](https://github.com/vsakkas/chatgpt-client/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/vsakkas/chatgpt-client/actions/workflows/main.yml)

Python client for the unofficial [ChatGPT](https://openai.com/blog/chatgpt/) API by [OpenAI](https://openai.com/).

## Installation

To install the ChatGPT Client, run the following command:

```bash
pip install chatgpt-client
```

## Usage

Sign up for an [OpenAI API key](https://platform.openai.com/overview) and store it in your environment.

```python
import asyncio
import os

from chatgpt_client import ChatGPTClient

async def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    client = ChatGPTClient(api_key)

    response = await client.get_completion("What is the meaning of life?")
    print(response["choices"][0]["text"])

if __name__ == "__main__":
    asyncio.run(main())
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/vsakkas/chatgpt-client/blob/master/LICENSE) file for details.
