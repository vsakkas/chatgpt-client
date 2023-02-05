# ChatGPT Client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/vsakkas/pychatgpt/actions/workflows/main.yml/badge.svg)](https://github.com/vsakkas/pychatgpt/actions/workflows/main.yml)

Python client for the unofficial [ChatGPT](https://openai.com/blog/chatgpt/) API by [OpenAI](https://openai.com/).

## Installation

To install the ChatGPT Client, run the following command:

```bash
pip install chatgpt-client
```

## Usage

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
